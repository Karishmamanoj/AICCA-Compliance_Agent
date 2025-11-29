from utils.logger import json_log

from agents.policy_reader import PolicyReaderAgent
from agents.compliance_checker import ComplianceCheckerAgent
from agents.report_generator import ReportGeneratorAgent

class SupervisorAgent:
    def __init__(self, memory=None, logger=None):
        self.memory = memory
        self.logger = logger

    def run_audit(self, policy_text, evidence_items, meta=None):

        trace_id = meta.get("trace_id", "no-trace-id")

        # --- LOG: Supervisor start ---
        if self.logger:
            self.logger.info(
                "Supervisor started audit",
                extra={"trace_id": trace_id, "component": "supervisor"}
            )
        json_log(trace_id, "supervisor", "info", "Supervisor started audit")

        # --- Policy extraction ---
        rules = PolicyReaderAgent().extract_rules(policy_text)

        if self.logger:
            self.logger.info(
                f"Extracted {len(rules)} rules",
                extra={"trace_id": trace_id, "component": "policy_reader"}
            )
        json_log(trace_id, "policy_reader", "info", f"Extracted {len(rules)} rules")

        # --- Compliance check ---
        results = ComplianceCheckerAgent().check(rules, evidence_items)

        if self.logger:
            self.logger.info(
                "Compliance check finished",
                extra={"trace_id": trace_id, "component": "compliance_checker"}
            )
        json_log(trace_id, "compliance_checker", "info", "Compliance check finished")

        # --- Report generation ---
        report = ReportGeneratorAgent().generate(results, meta)

        # Save memory
        if self.memory:
            self.memory.save_report(report)

        # --- LOG: Supervisor finish ---
        if self.logger:
            self.logger.info(
                "Supervisor finished audit",
                extra={"trace_id": trace_id, "component": "supervisor"}
            )
        json_log(trace_id, "supervisor", "info", "Supervisor finished audit")

        return report, results
