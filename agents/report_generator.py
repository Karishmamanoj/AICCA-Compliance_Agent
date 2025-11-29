class ReportGeneratorAgent:
    def generate(self, results, meta=None):
        meta = meta or {}
        report_lines = []
        report_lines.append("=== AICCA COMPLIANCE REPORT ===")
        if meta.get("policy_name"):
            report_lines.append(f"Policy: {meta['policy_name']}")
        report_lines.append("")
        for r in results:
            status = "PASS" if r["pass"] else "FAIL"
            report_lines.append(f"{status} - {r['rule']}")
        report_lines.append("")
        report_lines.append("Recommendations:")
        for r in results:
            if not r["pass"]:
                report_lines.append(f"- Review control: {r['rule']}")
        return "\n".join(report_lines)
