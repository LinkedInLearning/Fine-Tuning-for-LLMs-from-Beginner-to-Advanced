# Fine-Tuning Your AI Models: from Beginner to Advanced
This is the repository for the LinkedIn Learning course `Fine-Tuning Your AI Models: from Beginner to Advanced`. The full course is available from [LinkedIn Learning][lil-course-url].

![lil-thumbnail-url]

## Course Description

Fine-tuning lets you adapt an open-weight language model to your own task, data, and brand voice. In this course, you'll learn a complete modern fine-tuning workflow by building a support-ticket assistant for Ridgeline Outfitters, a fictional outdoor gear retailer. You'll prepare and validate training data, fine-tune a model with LoRA on a free GPU, score it against the base model, and run your finished model on your own laptop with Ollama. Along the way, you'll practice prompting, synthetic data generation, and evaluation design in hands-on exercises. By the end, you'll know when fine-tuning beats prompting alone and how to deliver a fine-tuned model with measurable business value.

## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get a message like this:

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

To resolve this issue:
	
    Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"

## Running the Notebooks in Google Colab
You run this course's notebooks in Google Colab, which gives you a free GPU in your browser. There's nothing to install on your own machine until the final chapter.

To open the notebook for any video:

1. Switch to that video's branch in GitHub, then open the `notebooks` folder and select the notebook.
2. Select the **Open in Colab** button at the top of the notebook. If you don't see one, copy the notebook's GitHub URL and replace `https://github.com/` with `https://colab.research.google.com/github/`.
3. In Colab, choose **Runtime > Change runtime type**, select **T4 GPU**, and select **Save**.
4. Choose **File > Save a copy in Drive** so your changes are saved to your own Google Drive.

Start with the GPU check notebook to confirm your setup:

| Notebook | Open |
| --- | --- |
| Check your GPU | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/<OWNER>/Fine-Tuning-for-LLMs-from-Beginner-to-Advanced/blob/main/notebooks/00_check_gpu.ipynb) |

Colab's free tier has usage limits, and idle sessions disconnect. If you lose your GPU mid-course, wait a while and reconnect, or load the checkpoint files in the `data` folder to pick up where you left off.

## Installing
1. To use these exercise files, you must have the following:
	- A free Google account, to run the notebooks in [Google Colab](https://colab.research.google.com)
	- A current web browser
	- For the final chapter only: [Ollama](https://ollama.com/download) installed on a computer with at least 8 GB of RAM and about 5 GB of free disk space
	- Optional: a free [Hugging Face account](https://huggingface.co/join), if you want to publish your fine-tuned model
2. Clone this repository into your local machine using the terminal (Mac), CMD (Windows), or a GUI tool like SourceTree. You only need a local copy for the final chapter, when you run your model with Ollama. Every other chapter runs in Colab.
3. Open `notebooks/00_check_gpu.ipynb` in Colab using the steps in **Running the Notebooks in Google Colab** and run both cells. If both print a success message, you're ready to start the course.

## Repo Layout
- `notebooks/` the Colab notebooks for each chapter, including begin and end versions for each challenge
- `data/` the Ridgeline Outfitters seed tickets and the checkpoint files for each chapter

## Instructor

Kesha Williams

Kesha Williams is an AWS AI Hero and the founder of Keysoft, an enterprise AI strategy, engineering, and education consultancy.

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/kesha-williams).


[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/
[lil-thumbnail-url]: https://media.licdn.com/dms/image/v2/D4E0DAQG0eDHsyOSqTA/learning-public-crop_675_1200/B4EZVdqqdwHUAY-/0/1741033220778?e=2147483647&v=beta&t=FxUDo6FA8W8CiFROwqfZKL_mzQhYx9loYLfjN-LNjgA
