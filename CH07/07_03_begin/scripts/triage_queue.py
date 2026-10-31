"""Run a queue of support tickets through your Ridgeline model and build a triage report.

Run from the CH07 folder, with Ollama running and your model named "ridgeline":
    python 07_03_begin/scripts/triage_queue.py
    python 07_03_begin/scripts/triage_queue.py --redteam path/to/redteam_tickets.json

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
    """Send one ticket to the model and return a row for the report.

    Return a dictionary with every key in COLUMNS:
      - category, escalate, reply: parsed from the model's output
      - expected_category: the ticket's category, or "any" if it has none
      - expected_escalate: the ticket's escalate value
      - triage_ok: True when the category and the escalate decision are both right
        (when a ticket has no expected category, any valid category counts)
      - voice_ok and failures: from ridgeline.check_reply
    """
    # TODO: write your solution here
    raise NotImplementedError("Write triage()")


def print_summary(rows):
    """Print what a support lead needs to see:
      - the escalation queue: every ticket the model escalated
      - missed escalations: tickets that should have been escalated but weren't
      - how many tickets landed in each category
      - triage and voice scores for the seed tickets and the red-team tickets
      - any reply with a broken Category/Escalate header
    """
    # TODO: write your solution here
    raise NotImplementedError("Write print_summary()")


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
