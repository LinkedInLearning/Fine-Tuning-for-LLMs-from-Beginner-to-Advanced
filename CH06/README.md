# Chapter 6: Evaluating Your Model

Each lesson with code has a begin folder with the starting code and an end folder with the finished code.

| Lesson | Begin | End |
| --- | --- | --- |
| 06_01 Compare your model to the baseline | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH06/06_01_begin/notebooks/06_01_compare_to_baseline.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH06/06_01_end/notebooks/06_01_compare_to_baseline.ipynb) |
| 06_02 Evaluate with an LLM judge | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH06/06_02_begin/notebooks/06_02_llm_judge.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH06/06_02_end/notebooks/06_02_llm_judge.ipynb) |
| 06_04 Challenge: Score your model against the baseline | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH06/06_04_begin/notebooks/06_04_score_challenge.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH06/06_04_end/notebooks/06_04_score_challenge.ipynb) |

## Shared files

- `ridgeline.py`: helpers every lesson in this chapter imports, for loading tickets, building prompts, and checking replies
- `data/`: the files this chapter uses

  - `eval_outputs.jsonl`: baseline and fine-tuned replies for every evaluation ticket, from 06_01
  - `eval.jsonl` and `synthetic_raw.jsonl`: the evaluation set and the tickets it came from
  - `ridgeline-seed-tickets.jsonl`, `policies.md`, and `voice_rules.md`: the Ridgeline tickets and rules
