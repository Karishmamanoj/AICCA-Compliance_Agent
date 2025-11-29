AICCA – AI Compliance & Controls Audit Agent
Automated Policy → Evidence → Compliance → Report Pipeline

🚀 Project Summary:

AICCA (AI Compliance & Controls Audit Agent) is a fully automated pipeline that reads security policies, extracts rules, evaluates system evidence, and generates auditor-grade compliance reports. It uses a multi-agent architecture, tools, memory, and structured logging, making it ideal for demonstrating end-to-end automation in cybersecurity compliance.

🧠 Key Features:

Multi-Agent System
Policy Reader Agent
Evidence Collector
Compliance Checker
Report Generator
Supervisor (Coordinator)

Tools Included"

TXT Reader
PDF Extractor
Evidence Fetch Simulator
Memory System
Session Memory
Long-Term Memory (JSON)
Logging
Console Log
JSONL Log
Trace-ID per run
Evaluation Notebooks
Accuracy testing
Completeness testing

📁 Folder Structure
AICCA/
├── agents/
├── tools/
├── memory/
├── utils/
├── evaluation/
├── docs/
├── logs/
├── main.py
└── requirements.txt

📘 How It Works

1️⃣ Policy Reader extracts rules from TXT/PDF
2️⃣ Evidence Collector simulates IT/SOC evidence
3️⃣ Compliance Checker compares rules vs. evidence
4️⃣ Report Generator builds full compliance report
5️⃣ Supervisor Agent orchestrates whole pipeline & logs events

▶️ Run the Pipeline

Install packages:

pip install -r requirements.txt


Run audit:
python main.py


You will see:

=== AICCA COMPLIANCE REPORT ===
PASS - Passwords must be at least 12 characters long.
PASS - MFA enabled for admin accounts.
...


🏗 Use Cases:

✔ SOC2 / ISO27001 audit simulation
✔ Security automation demos
✔ LLM multi-agent research
✔ AI compliance tools
✔ Capstone / academic projects

📦 Tech Stack:

Python
Multi-Agent Architecture
PDF and text parsing

JSON logging:
Notebook-based evaluation

🧑‍💻 Author

Karishma Manoj — AI Compliance Automation
