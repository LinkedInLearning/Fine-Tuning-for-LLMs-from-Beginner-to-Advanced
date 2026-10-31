"""Send one Ridgeline ticket to your model in Ollama and check the reply.

Run from the CH07 folder, with Ollama running and your model named "ridgeline":
    python 07_01_end/scripts/ask_ridgeline.py
    python 07_01_end/scripts/ask_ridgeline.py RT-008
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # the chapter folder
sys.path.insert(0, str(ROOT))
import ridgeline  # noqa: E402

ticket_id = sys.argv[1] if len(sys.argv) > 1 else "RT-001"
ticket = {t["id"]: t for t in ridgeline.load_tickets()}[ticket_id]

print(f"{ticket['customer_name']}: {ticket['subject']}")
print(f"{ticket['message']}\n")

messages = ridgeline.build_messages(ticket, include_voice_rules=False)
reply = ridgeline.ollama_chat(messages)

print(reply, "\n")
ridgeline.print_check(ridgeline.check_reply(ticket, reply))
