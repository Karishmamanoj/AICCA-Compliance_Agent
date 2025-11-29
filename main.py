print(">>> main.py started")

# -------------------------
# IMPORTS (you were missing all these)
# -------------------------
from utils.logger import get_logger, new_trace_id, json_log
from tools.file_reader_tool import read_text
from tools.evidence_fetch_tool import get_dummy_evidence
from agents.supervisor import SupervisorAgent
from memory.long_term_memory import LongTermMemory


# -------------------------
# MAIN FUNCTION
# -------------------------
def main():
    print(">>> ENTERED main()")

    # Create logger + trace ID
    logger = get_logger()
    trace_id = new_trace_id()

    logger.info("Starting audit run", extra={"trace_id": trace_id, "component": "main"})
    json_log(trace_id, "main", "info", "Starting audit run")

    # Read sample policy
    print(">>> Reading policy file...")
    policy_text = read_text("docs/policies/policy.txt")

    # Get dummy evidence
    print(">>> Fetching dummy evidence...")
    evidence = get_dummy_evidence()

    # Create memory storage
    memory = LongTermMemory("memory.json")

    # Create supervisor agent
    supervisor = SupervisorAgent(memory=memory, logger=logger)

    print(">>> Running audit...")
    report, results = supervisor.run_audit(
        policy_text,
        evidence,
        meta={"policy_name": "Sample Policy", "trace_id": trace_id}
    )

    logger.info("Audit completed", extra={"trace_id": trace_id, "component": "main"})
    json_log(trace_id, "main", "info", "Audit completed")

    print("\n===== FINAL REPORT =====\n")
    print(report)
    print("\n========================\n")

    print(">>> main() execution completed.")


# -------------------------
# ENTRY POINT
# -------------------------
if __name__ == "__main__":
    print(">>> calling main()...")
    main()
    print(">>> main() finished")
