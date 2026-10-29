import copy
from datetime import date, timedelta
import json
from pathlib import Path
import tempfile
import unittest

from tools import procedure_model as pm


class ProceduralModelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model, cls.sources = pm.load_package()
        cls.cases = pm.read_json(pm.ROOT / "examples.json")["cases"]

    def case(self, name="gateway2-no-draft-plan"):
        return copy.deepcopy(next(c for c in self.cases if c["id"] == name))

    def test_schema_references_and_all_examples(self):
        pm.validate_model(self.model, self.sources)
        self.assertEqual(pm.run_examples(self.model, self.sources), len(self.cases))

    def test_guidance_cannot_be_promoted_to_legislation(self):
        model = copy.deepcopy(self.model)
        rule = next(r for r in model["rules"] if r["id"] == "new.gateway2_draft_plan")
        rule["status"] = "statutory"
        with self.assertRaisesRegex(ValueError, "no legislative basis"):
            pm.validate_model(model, self.sources)
        rule["sources"][0]["role"] = "legal_basis"
        with self.assertRaisesRegex(ValueError, "guidance cannot"):
            pm.validate_model(model, self.sources)

    def test_statutory_rules_need_primary_verification(self):
        model = copy.deepcopy(self.model)
        model["rules"][0]["verification"]["level"] = "guidance_checked"
        with self.assertRaisesRegex(ValueError, "primary-text"):
            pm.validate_model(model, self.sources)

    def test_unknown_source_and_cross_regime_stage_are_rejected(self):
        model = copy.deepcopy(self.model)
        model["rules"][0]["sources"][0]["source"] = "imagined-source"
        with self.assertRaisesRegex(ValueError, "unknown source"):
            pm.validate_model(model, self.sources)
        model = copy.deepcopy(self.model)
        model["rules"][0]["stage"] = "new.gateway2"
        with self.assertRaisesRegex(ValueError, "stage/regime mismatch"):
            pm.validate_model(model, self.sources)

    def test_unknown_predicate_cannot_pass(self):
        model = copy.deepcopy(self.model)
        model["rules"][0]["check"] = {"op": "ask_an_llm"}
        with self.assertRaises(ValueError):
            pm.validate_model(model, self.sources)

    def test_inverted_validity_and_future_verification_rejected(self):
        for change in ("interval", "verification"):
            model = copy.deepcopy(self.model)
            if change == "interval":
                model["rules"][0]["temporal"]["effective_to"] = "2025-01-01"
            else:
                model["rules"][0]["verification"]["checked_on"] = "2099-01-01"
            with self.assertRaises(ValueError):
                pm.validate_model(model, self.sources)

    def test_evidence_reference_integrity(self):
        case = self.case()
        case["facts"]["gateway2_necessary_material_sent"]["evidence_refs"] = ["missing"]
        with self.assertRaisesRegex(ValueError, "missing evidence"):
            pm.validate_case(case, self.model)

    def test_routing_retains_direction_and_submission_evidence(self):
        case = self.case("late-legacy-directed")
        case["evidence"].append({"id": "direction", "kind": "decision",
                                 "locator": "synthetic:direction", "note": "Test only"})
        case["facts"]["legacy_direction_verified"]["evidence_refs"] = ["direction"]
        result = pm.evaluate(case, self.model, self.sources)
        self.assertIn("direction", result["route"]["evidence_refs"])
        self.assertIn("submission_date", result["route"]["facts_considered"])
        self.assertTrue(result["route"]["source_details"][0]["version"])

    def test_false_and_null_are_different(self):
        case = self.case()
        key = "new_gateway2_plan_provided"
        case["facts"][key]["value"] = None
        result = pm.evaluate(case, self.model, self.sources)
        self.assertEqual(result["results"][0]["status"], "unknown")
        case["facts"][key]["value"] = False
        result = pm.evaluate(case, self.model, self.sources)
        self.assertEqual(result["results"][0]["status"], "advisory_gap")

    def test_boolean_strings_are_not_truthy_observations(self):
        case = self.case()
        case["facts"]["gateway2_necessary_material_sent"]["value"] = "false"
        with self.assertRaisesRegex(ValueError, "JSON boolean"):
            pm.validate_case(case, self.model)

    def test_unknown_fact_or_rule_is_rejected(self):
        for kind in ("fact", "rule"):
            case = self.case()
            if kind == "fact":
                case["facts"]["typo"] = {"value": True, "evidence_refs": ["fixture"]}
            else:
                case["rule_ids"].append("new.nonexistent")
            with self.assertRaisesRegex(ValueError, "Unknown"):
                pm.validate_case(case, self.model)

    def test_invalid_calendar_dates_rejected(self):
        case = self.case("new-plan-eight-weeks")
        case["facts"]["consultation_deadline"]["value"] = "2026-02-30"
        with self.assertRaisesRegex(ValueError, "invalid ISO"):
            pm.validate_case(case, self.model)

    def test_week_periods_across_leap_days_and_year_boundaries(self):
        expr = {"op": "date_gap_at_least", "start": "a", "end": "b", "days": 42}
        for start in (date(2028, 2, 1), date(2026, 12, 15)):
            for days in (41, 42, 43):
                facts = {"a": {"value": start.isoformat()},
                         "b": {"value": (start + timedelta(days=days)).isoformat()}}
                self.assertEqual(pm.evaluate_expression(expr, facts), days >= 42)

    def test_three_valued_logic(self):
        missing = {"op": "eq", "fact": "missing", "value": True}
        true = {"op": "constant", "value": True}
        false = {"op": "constant", "value": False}
        for op, args, expected in (("all", [missing, true], None),
                                   ("all", [missing, false], False),
                                   ("any", [missing, true], True),
                                   ("any", [missing, false], None)):
            self.assertIs(pm.evaluate_expression({"op": op, "args": args}, {}), expected)

    def test_duplicates_rejected_in_json_and_collections(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "duplicate.json"
            path.write_text('{"a":true,"a":false}')
            with self.assertRaisesRegex(ValueError, "Duplicate JSON"):
                pm.read_json(path)
        model = copy.deepcopy(self.model)
        model["rules"].append(model["rules"][0])
        with self.assertRaisesRegex(ValueError, "Duplicate rules"):
            pm.validate_model(model, self.sources)

    def test_no_automatic_regime_switch_from_date(self):
        for day in ("2026-12-30", "2026-12-31", "2027-01-01"):
            case = self.case("unknown-route-on-boundary")
            case["facts"]["submission_date"]["value"] = day
            self.assertEqual(pm.select_regime(case, self.model)["regime"], "unknown")

    def test_output_carries_source_version_and_fact_provenance(self):
        report = pm.evaluate(self.case(), self.model, self.sources)
        self.assertEqual(report["knowledge_date"], "2026-10-29")
        for result in report["results"]:
            self.assertTrue(result["sources"][0]["version"])
            self.assertTrue(result["sources"][0]["url"].startswith("https://"))
            self.assertEqual(result["evidence_refs"], ["fixture"])
        self.assertNotIn("plan_compliant", report)

    def test_obsolete_duties_are_not_reintroduced(self):
        statutory = [r for r in self.model["rules"] if r["status"] == "statutory"]
        self.assertFalse(any("paper form" in r["statement"] for r in statutory))
        self.assertFalse(any("duty to co-operate" in r["statement"].lower() for r in statutory))
        self.assertIn("expressly excluded", json.dumps(self.model["regimes"]))


if __name__ == "__main__":
    unittest.main()
