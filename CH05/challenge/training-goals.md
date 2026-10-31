# Training goals: Ridgeline support assistant

## What the model has to do
- Read a Ridgeline Outfitters support ticket plus what the support system knows about it.
- Reply in exactly this format: a Category line, an Escalate line, a blank line, then a reply in the Ridgeline brand voice.
- Choose one of six categories and decide whether to escalate.
- Learn the brand voice from the training replies. The voice rules are not in the prompt.

## Constraints
- Base model: Qwen3 4B Instruct, loaded in 4-bit (QLoRA) with Unsloth.
- Hardware: one free Google Colab T4 GPU with about 15 GB of memory.
- Time budget: the training run should finish in about 20 minutes on a free T4.
- Maximum sequence length: 2,048 tokens.

## What good looks like
- Evaluation loss ends lower than where it started and doesn't climb back up near the end.
- Replies to unseen tickets use the exact header format and the Ridgeline sign-off.
- The model still answers ordinary questions normally, without forcing them into ticket format.
