"""Generate synthetic Ridgeline support tickets with Claude.

Run from the CH04 folder:
    pip install anthropic
    export ANTHROPIC_API_KEY=your-key
    python 04_02_end/scripts/generate_synthetic.py

Writes every generated ticket to data/synthetic_raw.jsonl. Nothing is filtered
here. You validate the examples in the next step.
"""
import argparse
import json
import os
import random
import re
import sys
from pathlib import Path

import anthropic

ROOT = Path(__file__).resolve().parents[2]  # the chapter folder
sys.path.insert(0, str(ROOT))
import ridgeline  # noqa: E402

MODEL = "claude-sonnet-5-5"

PRODUCTS = [
    "Cascade 65 backpack", "Ember 15 daypack", "Talus hiking boots", "Switchback trekking poles",
    "Firn 20 sleeping bag", "Meridian rain shell", "Sawtooth insulated jacket", "Basecamp 4 tent",
    "Ridgerunner trail socks",
]
STYLES = [
    "short and blunt", "angry", "polite and detailed", "rambling first-timer",
    "confused", "in a hurry", "friendly regular customer",
]

PROMPT = """You write training data for the customer support assistant at Ridgeline Outfitters, an outdoor gear retailer.

Write {n} new support tickets in the category "{category}", each with the ideal reply.

Requirements:
- Return each ticket as a JSON object with these keys: customer_name, subject, message, context, escalate, reply.
- reply is only the message the customer reads. It starts with the greeting. Don't put Category or Escalate lines in it.
- Spread these customer styles across the batch: {styles}.
- Mention products from this catalog: {products}.
- context is what the support system knows about the customer: order IDs like RO-48213, dates, order status, purchase verification, and policy flags.
- The reply may only use facts from the ticket, the context, and the policies. Never invent tracking numbers, dates, or order details.
- About {escalation_pct} percent of the tickets should need escalation under the policies. Set escalate to "Yes" for those and "No" for the rest.
- Every reply follows every voice rule below exactly.
- Invent customer names. Never include email addresses, phone numbers, street addresses, or card numbers.
- Make every ticket different from the examples and from each other.

Policies:
{policies}

Voice rules:
{voice_rules}

Finished examples:
{examples}

Return only a JSON array of {n} objects inside <tickets></tickets> tags."""


def build_prompt(category, n, seeds):
    same = [t for t in seeds if t["category"] == category]
    others = random.sample([t for t in seeds if t["category"] != category], 2)
    keys = ("customer_name", "subject", "message", "context", "escalate", "reply")
    examples = json.dumps([{k: t[k] for k in keys} for t in same + others], indent=2)
    return PROMPT.format(
        n=n,
        category=category,
        styles=", ".join(random.sample(STYLES, 4)),
        products=", ".join(PRODUCTS),
        escalation_pct=15,
        policies=ridgeline.policies(),
        voice_rules=ridgeline.voice_rules(),
        examples=examples,
    )


# Some batches still put the Category and Escalate lines inside the reply.
REPLY_HEADER = re.compile(r"^\s*Category:[^\n]*\n\s*Escalate:[^\n]*\n+", re.IGNORECASE)


def parse_tickets(text):
    match = re.search(r"<tickets>(.*)</tickets>", text, re.DOTALL)
    if not match:
        return []
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError:
        return []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--per-category", type=int, default=85)
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--out", default=str(ROOT / "data" / "synthetic_raw.jsonl"))
    args = parser.parse_args()

    random.seed(42)
    client = anthropic.Anthropic()
    seeds = ridgeline.load_tickets()
    out_path = Path(args.out).resolve()
    tokens_in = tokens_out = 0
    total = 0

    with out_path.open("w") as f:
        for category in ridgeline.CATEGORIES:
            made = 0
            failures = 0
            while made < args.per_category:
                n = min(args.batch_size, args.per_category - made)
                response = client.messages.create(
                    model=MODEL,
                    max_tokens=16000,
                    messages=[{"role": "user", "content": build_prompt(category, n, seeds)}],
                )
                tokens_in += response.usage.input_tokens
                tokens_out += response.usage.output_tokens
                text = "".join(b.text for b in response.content if b.type == "text")
                batch = parse_tickets(text)
                if not batch:
                    failures += 1
                    reason = "it hit the output limit" if response.stop_reason == "max_tokens" else "the format was off"
                    print(f"  {category}: could not read a batch because {reason}, retrying")
                    if failures == 3:
                        sys.exit("Stopped after 3 unreadable batches in a row. Try a smaller --batch-size.")
                    continue
                failures = 0
                for ticket in batch[:n]:
                    total += 1
                    ticket["id"] = f"SYN-{total:04d}"
                    ticket["category"] = category
                    ticket["reply"] = REPLY_HEADER.sub("", ticket.get("reply", "")).strip()
                    f.write(json.dumps(ticket, ensure_ascii=False) + "\n")
                made += len(batch[:n])
                print(f"  {category}: {made}/{args.per_category}")

    print(f"\nWrote {total} tickets to {os.path.relpath(out_path, ROOT)}")
    print(f"Tokens used: {tokens_in:,} in, {tokens_out:,} out")


if __name__ == "__main__":
    main()
