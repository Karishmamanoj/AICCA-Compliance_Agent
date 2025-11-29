class ComplianceCheckerAgent:
    def check(self, rules, evidence):
        results = []
        for rule in rules:
            rule_lower = rule.lower()
            matched = False
            for e in evidence:
                if e.lower() in rule_lower or e.lower() in rule:
                    matched = True
                    break
            results.append({"rule": rule, "pass": matched})
        return results
