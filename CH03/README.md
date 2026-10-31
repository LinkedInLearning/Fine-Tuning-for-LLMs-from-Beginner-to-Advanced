# Chapter 3: Setting Up Your Fine-Tuning Environment

Each lesson with code has a begin folder with the starting code and an end folder with the finished code.

| Lesson | Begin | End |
| --- | --- | --- |
| 03_03 Load the base model and test it on a ticket | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH03/03_03_begin/notebooks/03_03_load_base_model.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH03/03_03_end/notebooks/03_03_load_base_model.ipynb) |

## Shared files

- `ridgeline.py`: helpers every lesson in this chapter imports, for loading tickets, building prompts, and checking replies
- `data/`: the files this chapter uses

  - `ridgeline-seed-tickets.jsonl`: the 18 hand-written seed tickets
  - `policies.md` and `voice_rules.md`: Ridgeline's support policies and brand voice rules

Run `notebooks/00_check_gpu.ipynb` first to confirm your Colab setup:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH03/notebooks/00_check_gpu.ipynb)
