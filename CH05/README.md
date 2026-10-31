# Chapter 5: Fine-Tuning with LoRA

Each lesson with code has a begin folder with the starting code and an end folder with the finished code.

| Lesson | Begin | End |
| --- | --- | --- |
| 05_01 Configure LoRA hyperparameters | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH05/05_01_begin/notebooks/05_01_configure_lora.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH05/05_01_end/notebooks/05_01_configure_lora.ipynb) |
| 05_02 Train the support assistant | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH05/05_02_begin/notebooks/05_02_train_the_assistant.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH05/05_02_end/notebooks/05_02_train_the_assistant.ipynb) |
| 05_03 Troubleshoot common training problems | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH05/05_03_begin/notebooks/05_03_troubleshoot_training.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH05/05_03_end/notebooks/05_03_troubleshoot_training.ipynb) |
| 05_04 Challenge: Fine-tune the support assistant | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH05/05_04_begin/notebooks/05_04_fine_tune_challenge.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH05/05_04_end/notebooks/05_04_fine_tune_challenge.ipynb) |

## Shared files

- `ridgeline.py`: helpers every lesson in this chapter imports, for loading tickets, building prompts, and checking replies
- `data/`: the files this chapter uses

  - `train.jsonl` and `eval.jsonl`: the finished dataset from Chapter 4
  - `ridgeline-seed-tickets.jsonl`, `policies.md`, and `voice_rules.md`: the Ridgeline tickets and rules
- `challenge/training-goals.md`: the goals and constraints for the 05_04 challenge
