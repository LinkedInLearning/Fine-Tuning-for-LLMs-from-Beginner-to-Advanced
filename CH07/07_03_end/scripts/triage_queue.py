"""Run a queue of support tickets through your Ridgeline model and build a triage report.

Run from the CH07 folder, with Ollama running and your model named "ridgeline":
    python 07_03_end/scripts/triage_queue.py
    python 07_03_end/scripts/triage_queue.py --redteam path/to/redteam_tickets.json

It sends the 18 seed tickets plus a red-team set through the model, saves
outputs/triage_report.csv, and prints the queue your support team would see.
"""
import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # the chapter folder
sys.path.insert(0, str(ROOT))
import ridgeline  # noqa: E402

REPORT = ROOT / "outputs" / "triage_report.csv"
COLUMNS = ["id", "source", "type", "subject", "category", "escalate", "expected_category",
           "expected_escalate", "triage_ok", "voice_ok", "failures", "reply"]


def load_queue(redteam_path):
    """The 18 seed tickets, followed by the red-team tickets."""
    queue = [dict(t, source="seed") for t in ridgeline.load_tickets()]
    queue += [dict(t, source="red-team") for t in ridgeline.load_ticket_file(redteam_path)]
    return queue


def triage(ticket):
    """Send one ticket to the model and return a row for the report."""
    output = ridgeline.ollama_chat(ridgeline.build_messages(ticket, include_voice_rules=False))
    parsed = ridgeline.parse_output(output)
    result = ridgeline.check_reply(ticket, output)

    # Ambiguous red-team tickets have no single right category, so any valid one counts.
    expected_category = ticket.get("category")
    category_ok = result["category_ok"] if expected_category else parsed["category"] in ridgeline.CATEGORIES

    return {
        "id": ticket["id"],
        "source": ticket["source"],
        "type": ticket.get("type", ""),
        "subject": ticket["subject"],
        "category": parsed["category"] or "",
        "escalate": parsed["escalate"] or "",
        "expected_category": expected_category or "any",
        "expected_escalate": ticket["escalate"],
        "triage_ok": category_ok and result["escalate_ok"],
        "voice_ok": result["voice_ok"],
        "failures": "; ".join(result["failures"]),
        "reply": parsed["reply"],
    }


def print_summary(rows):
    """Print the escalation queue, the category counts, and how well the model did."""
    escalations = [r for r in rows if r["escalate"] == "Yes"]
    print(f"\nESCALATION QUEUE: {len(escalations)} tickets for a specialist")
    for r in escalations:
        print(f"  {r['id']}  {r['subject']}")

    missed = [r for r in rows if r["expected_escalate"] == "Yes" and r["escalate"] != "Yes"]
    print(f"\nMISSED ESCALATIONS: {len(missed)}")
    for r in missed:
        print(f"  {r['id']}  {r['subject']}")

    print("\nTICKETS BY CATEGORY")
    for category, count in Counter(r["category"] or "(no category)" for r in rows).most_common():
        print(f"  {count:>2}  {category}")

    print("\nSCORES")
    for source in ["seed", "red-team"]:
        group = [r for r in rows if r["source"] == source]
        if group:
            triage_ok = sum(r["triage_ok"] for r in group)
            voice_ok = sum(r["voice_ok"] for r in group)
            print(f"  {source:<9} triage {triage_ok}/{len(group)}   voice {voice_ok}/{len(group)}")

    broken = [r for r in rows if "Category/Escalate header" in r["failures"]]
    if broken:
        print("\nFORMAT FAILURES: replies a support system couldn't route")
        for r in broken:
            print(f"  {r['id']}  {r['subject']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--redteam", default=str(ridgeline.DATA / "redteam_tickets.jsonl"))
    args = parser.parse_args()

    queue = load_queue(args.redteam)
    print(f"Triaging {len(queue)} tickets with your Ridgeline model...")
    rows = []
    for i, ticket in enumerate(queue, start=1):
        rows.append(triage(ticket))
        print(f"  [{i:>2}/{len(queue)}] {ticket['id']}")

    REPORT.parent.mkdir(exist_ok=True)
    with REPORT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nSaved {REPORT.relative_to(ROOT)}")

    print_summary(rows)


if __name__ == "__main__":
    main()
