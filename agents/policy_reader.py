class PolicyReaderAgent:
    def extract_rules(self, text):
        rules = []
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            lower = line.lower()
            if any(k in lower for k in ("must", "should", "required", "shall", "mandatory")):
                rules.append(line)
        return rules
