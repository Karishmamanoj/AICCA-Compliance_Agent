# AICCA — AI Compliance Copilot for Automated Audits

## Summary
AICCA reads policy text, extracts compliance rules, validates evidence, and generates structured audit reports using a multi-agent architecture.

## Quick start
1. Clone repo
2. `python -m venv venv && venv\Scripts\activate`
3. `pip install -r requirements.txt`
4. `python main.py`

## Folder layout
- agents/ — PolicyReader, ComplianceChecker, ReportGenerator, Supervisor
- tools/ — file reader, evidence tool
- utils/ — logger
- docs/policies/ — sample policies
- logs/ — runtime logs
- memory.json — stored reports

## Note
This is a capstone prototype. See docs/final_report.md for full design, evaluation, and next steps.
