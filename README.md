# Fine-Tuning Your AI Models: from Beginner to Advanced
This is the repository for the LinkedIn Learning course `Fine-Tuning Your AI Models: from Beginner to Advanced`. The full course is available from [LinkedIn Learning][lil-course-url].

![lil-thumbnail-url]

## Course Description

Fine-tuning lets you adapt an open-weight language model to your own task, data, and brand voice. In this course, you'll learn a complete modern fine-tuning workflow by building a support-ticket assistant for Ridgeline Outfitters, a fictional outdoor gear retailer. You'll prepare and validate training data, fine-tune a model with LoRA on a free GPU, score it against the base model, and run your finished model on your own laptop with Ollama. Along the way, you'll practice prompting, synthetic data generation, and evaluation design in hands-on exercises. By the end, you'll know when fine-tuning beats prompting alone and how to deliver a fine-tuned model with measurable business value.

## Instructions
This repository has a folder for each chapter of the course that includes code: `CH03` through `CH07`.

Inside each chapter folder, every lesson with code has two folders. The folder ending in `_begin` holds the code as it is at the beginning of the video. The folder ending in `_end` holds the code as it is at the end of the video. For example, `CH03/03_03_begin` and `CH03/03_03_end` go with video 03_03, the third video in chapter 3.

Every chapter folder also has its own `ridgeline.py` helper file and `data` folder, so each chapter works on its own. If you skip a challenge, the next chapter still has the files it needs. Each chapter folder has a README with links to its notebooks.

## Running the Notebooks in Google Colab
You run this course's notebooks in Google Colab, which gives you a free GPU in your browser. There's nothing to install on your own machine until the final chapter.

To open the notebook for any video:

1. Open the chapter folder, then the lesson's `_begin` or `_end` folder, then the `notebooks` folder, and select the notebook.
2. Select the **Open in Colab** button at the top of the notebook. Every chapter README also has these buttons. If you don't see one, copy the notebook's GitHub URL and replace `https://github.com/` with `https://colab.research.google.com/github/`.
3. In Colab, choose **Runtime > Change runtime type**, select **T4 GPU**, and select **Save**.
4. Choose **File > Save a copy in Drive** so your changes are saved to your own Google Drive.

Start with the GPU check notebook to confirm your setup:

| Notebook | Open |
| --- | --- |
| Check your GPU | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/LinkedInLearning/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/CH03/notebooks/00_check_gpu.ipynb) |

Colab's free tier has usage limits, and idle sessions disconnect. If you lose your GPU mid-course, wait a while and reconnect, or move on to the next chapter, which has its own copy of the files it needs.

## Installing
1. To use these exercise files, you must have the following:
	- A free Google account, to run the notebooks in [Google Colab](https://colab.research.google.com)
	- A current web browser
	- For the final chapter only: [Ollama](https://ollama.com/download) installed on a computer with at least 8 GB of RAM and about 5 GB of free disk space, plus Python 3
	- Optional: a free [Hugging Face account](https://huggingface.co/join), if you want to publish your fine-tuned model
2. Clone this repository into your local machine using the terminal (Mac), CMD (Windows), or a GUI tool like SourceTree. You only need a local copy for the final chapter, when you run your model with Ollama. Every other chapter runs in Colab.
3. Open `CH03/notebooks/00_check_gpu.ipynb` in Colab using the steps in **Running the Notebooks in Google Colab** and run both cells. If both print a success message, you're ready to start the course.

## Repo Layout
- `CH03` to `CH07`: one folder per chapter with code
  - `XX_YY_begin` and `XX_YY_end`: the starting and finished code for each lesson
  - `ridgeline.py`: shared helpers for the Ridgeline Outfitters project
  - `data`: the tickets, policies, and checkpoint files the chapter uses

## Instructor

Kesha Williams

Kesha Williams is an AWS AI Hero and the founder of Keysoft, an enterprise AI strategy, engineering, and education consultancy.

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/kesha-williams).


[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/
[lil-thumbnail-url]: https://media.licdn.com/dms/image/v2/D4E0DAQG0eDHsyOSqTA/learning-public-crop_675_1200/B4EZVdqqdwHUAY-/0/1741033220778?e=2147483647&v=beta&t=FxUDo6FA8W8CiFROwqfZKL_mzQhYx9loYLfjN-LNjgA
