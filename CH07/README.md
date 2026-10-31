# Chapter 7: Deploying and Using Your Model

Each lesson with code has a begin folder with the starting code and an end folder with the finished code.

| Lesson | Begin | End |
| --- | --- | --- |
| 07_01 Merge your model and run it locally with Ollama | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH07/07_01_begin/notebooks/07_01_export_for_ollama.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH07/07_01_end/notebooks/07_01_export_for_ollama.ipynb) |
| 07_03 Challenge: Put the assistant to work | [`07_03_begin/scripts/triage_queue.py`](07_03_begin/scripts/triage_queue.py) | [`07_03_end/scripts/triage_queue.py`](07_03_end/scripts/triage_queue.py) |

## Shared files

- `ridgeline.py`: helpers every lesson in this chapter imports, for loading tickets, building prompts, and checking replies
- `data/`: the files this chapter uses

  - `redteam_tickets.jsonl`: 12 adversarial tickets for the capstone
  - `ridgeline-seed-tickets.jsonl`, `policies.md`, and `voice_rules.md`: the Ridgeline tickets and rules

Run the scripts from this chapter folder, for example:

```
python 07_03_begin/scripts/triage_queue.py
```

- `ollama/Modelfile`: tells Ollama how to load and run the model you export in 07_01
- `ollama/Modelfile.hf`: loads the instructor's published model with the same chat template, for learners who skipped training
