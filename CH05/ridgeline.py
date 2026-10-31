"""Shared helpers for the Ridgeline Outfitters course project.

Every notebook imports this file, so the tickets, prompts, and scoring rules
stay the same from chapter to chapter.
"""
import json
import re
from pathlib import Path

DATA = Path(__file__).parent / "data"

CATEGORIES = [
    "Order Status", "Returns & Exchanges", "Warranty & Repairs",
    "Product Question", "Shipping Issue", "Billing & Account",
]
BANNED_PHRASES = [
    "we apologize for any inconvenience", "per our policy", "valued customer",
    "at this time", "please be advised", "sorry for the trouble",
]
SIGN_OFF = "Happy trails,\nThe Ridgeline Crew"
MAX_WORDS = 120

INSTRUCTIONS = (
    "You are the customer support assistant for Ridgeline Outfitters, an outdoor gear retailer. "
    "Classify the ticket, decide whether to escalate, and write the reply in the required format."
)


def load_tickets(path=DATA / "ridgeline-seed-tickets.jsonl"):
    """Read a JSONL file of tickets into a list of dictionaries."""
    return [json.loads(line) for line in Path(path).read_text().splitlines() if line.strip()]


def policies():
    return (DATA / "policies.md").read_text().strip()


def voice_rules():
    return (DATA / "voice_rules.md").read_text().strip()


def build_messages(ticket, include_voice_rules=True):
    """Build the chat messages for one ticket.

    The prompt-only baseline includes the full voice rules. The fine-tuned
    model leaves them out, because it learns the voice from training.
    """
    system = f"{INSTRUCTIONS}\n\n{policies()}"
    if include_voice_rules:
        system += f"\n\n{voice_rules()}"
    user = (
        f"Customer: {ticket['customer_name']}\n"
        f"Subject: {ticket['subject']}\n\n"
        f"{ticket['message']}\n\n"
        f"What the support system knows: {ticket['context']}"
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def gold_output(ticket):
    """The ideal model output for a ticket: two header lines, a blank line, then the reply."""
    return f"Category: {ticket['category']}\nEscalate: {ticket['escalate']}\n\n{ticket['reply']}"


def parse_output(text):
    """Split a model output into its Category, Escalate, and reply parts."""
    # Drop an empty <think></think> block if the model adds one.
    text = THINK_BLOCK.sub("", text)
    # Strip trailing spaces, which models often add as Markdown line breaks.
    lines = [line.rstrip() for line in text.strip().splitlines()]
    cat = re.match(r"^Category:\s*(.+)$", lines[0].strip()) if lines else None
    esc = re.match(r"^Escalate:\s*(Yes|No)\s*$", lines[1].strip()) if len(lines) > 1 else None
    reply = "\n".join(lines[2:]).strip() if cat and esc else text.strip()
    return {
        "category": cat.group(1).strip() if cat else None,
        "escalate": esc.group(1) if esc else None,
        "reply": reply,
    }


def check_reply(ticket, output):
    """Score one output against the triage labels and the voice rules."""
    parsed = parse_output(output)
    reply = parsed["reply"]
    first_name = ticket["customer_name"].split()[0]
    failures = []

    if parsed["category"] is None or parsed["escalate"] is None:
        failures.append("missing or broken Category/Escalate header")
    elif parsed["category"] not in CATEGORIES:
        failures.append(f"unknown category '{parsed['category']}'")
    if not reply.startswith(f"Hi {first_name},"):
        failures.append("greeting is not 'Hi <first name>,'")
    if not reply.rstrip().endswith(SIGN_OFF):
        failures.append("sign-off is not 'Happy trails, / The Ridgeline Crew'")
    words = len(reply.split())
    if words > MAX_WORDS:
        failures.append(f"too long ({words} words)")
    lowered = reply.lower()
    failures += [f"banned phrase: '{p}'" for p in BANNED_PHRASES if p in lowered]
    if reply.count("!") > 1:
        failures.append(f"{reply.count('!')} exclamation marks")

    return {
        "id": ticket["id"],
        "category_ok": parsed["category"] == ticket.get("category"),
        "escalate_ok": parsed["escalate"] == ticket.get("escalate"),
        "voice_ok": not failures,
        "failures": failures,
    }


def print_check(result):
    """Print a check_reply result in a readable way."""
    triage = "correct" if result["category_ok"] and result["escalate_ok"] else "WRONG"
    print(f"{result['id']}  triage: {triage}")
    if result["voice_ok"]:
        print("  voice: passed every rule")
    for failure in result["failures"]:
        print(f"  voice miss: {failure}")


def save_jsonl(rows, path):
    """Write a list of dictionaries to a JSONL file, one per line."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def to_training_example(ticket):
    """Turn a ticket into a chat-format training example.

    The system prompt leaves out the voice rules. The assistant turn is the
    ideal output, so the model learns the Ridgeline voice from examples.
    """
    messages = build_messages(ticket, include_voice_rules=False)
    messages.append({"role": "assistant", "content": gold_output(ticket)})
    return {
        "id": ticket["id"],
        "category": ticket["category"],
        "escalate": ticket["escalate"],
        "messages": messages,
    }


THINK_BLOCK = re.compile(r"<think>\s*</think>\s*")


def chat_text(tokenizer, messages, add_generation_prompt=False):
    """Render messages with the model's chat template.

    Qwen3's template adds an empty <think></think> block to finished assistant
    turns. This model doesn't reason out loud, so the block is removed. That way
    the model never learns to start a reply with empty tags.
    """
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=add_generation_prompt)
    return THINK_BLOCK.sub("", text)


def count_tokens(tokenizer, messages, add_generation_prompt=False):
    """Count the tokens in a conversation after the chat template is applied."""
    text = chat_text(tokenizer, messages, add_generation_prompt)
    return len(tokenizer(text, add_special_tokens=False)["input_ids"])


def generate(model, tokenizer, messages, max_new_tokens=400, sample=False):
    """Generate a reply for a list of chat messages.

    sample=False always picks the most likely next token, so results repeat.
    sample=True adds some randomness, like a production assistant would.
    """
    prompt = chat_text(tokenizer, messages, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    options = {"max_new_tokens": max_new_tokens, "do_sample": sample}
    if sample:
        options.update(temperature=0.7, top_p=0.8)
    output_ids = model.generate(**inputs, **options)
    new_tokens = output_ids[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()


def load_eval_tickets(eval_path=DATA / "eval.jsonl"):
    """Return the full ticket record for every example in the evaluation set."""
    ids = [json.loads(line)["id"] for line in Path(eval_path).read_text().splitlines() if line.strip()]
    pool = {t["id"]: t for t in load_tickets()}
    raw = DATA / "synthetic_raw.jsonl"
    if raw.exists():
        pool.update({t["id"]: t for t in load_tickets(raw)})
    return [pool[i] for i in ids]


def ollama_chat(messages, model="ridgeline", host="http://localhost:11434"):
    """Send chat messages to a model running in Ollama and return its reply.

    Uses only the Python standard library, so there's nothing extra to install.
    """
    import urllib.request

    body = json.dumps({
        "model": model,
        "messages": messages,
        "stream": False,
        "options": {"temperature": 0},
    }).encode()
    request = urllib.request.Request(f"{host}/api/chat", data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=300) as response:
        return json.loads(response.read())["message"]["content"].strip()


def load_ticket_file(path):
    """Read tickets from a JSON array file or a JSONL file."""
    text = Path(path).read_text().strip()
    return json.loads(text) if text.startswith("[") else load_tickets(path)
