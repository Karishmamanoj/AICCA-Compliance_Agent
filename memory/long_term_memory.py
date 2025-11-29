import json
from pathlib import Path

class LongTermMemory:
    def __init__(self, path="memory.json"):
        self.path = Path(path)

    def save_report(self, report_text):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps({"report": report_text}) + "\n")
