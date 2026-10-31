# Chapter 4: Preparing Data for Fine-Tuning

Each lesson with code has a begin folder with the starting code and an end folder with the finished code.

| Lesson | Begin | End |
| --- | --- | --- |
| 04_02 Generate synthetic examples with a frontier model | None | [`04_02_end/scripts/generate_synthetic.py`](04_02_end/scripts/generate_synthetic.py) |
| 04_04 Format data with chat templates | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH04/04_04_begin/notebooks/04_04_format_chat_templates.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH04/04_04_end/notebooks/04_04_format_chat_templates.ipynb) |
| 04_05 Split and validate your dataset | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH04/04_05_begin/notebooks/04_05_validate_and_split.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH04/04_05_end/notebooks/04_05_validate_and_split.ipynb) |
| 04_06 Challenge: Build the Ridgeline training dataset | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH04/04_06_begin/notebooks/04_06_build_training_dataset.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH04/04_06_end/notebooks/04_06_build_training_dataset.ipynb) |

## Shared files

- `ridgeline.py`: helpers every lesson in this chapter imports, for loading tickets, building prompts, and checking replies
- `data/`: the files this chapter uses

  - `ridgeline-seed-tickets.jsonl`: the 18 hand-written seed tickets
  - `synthetic_raw.jsonl`: about 500 generated tickets from 04_02, before any checks
  - `policies.md` and `voice_rules.md`: Ridgeline's support policies and brand voice rules

Run the scripts from this chapter folder, for example:

```
python 04_02_end/scripts/generate_synthetic.py
```
