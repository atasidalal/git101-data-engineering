## Chapter 5 Practice
Successfully configured and verified my GitHub remote tracking layout!

# GitHub Remotes

## Objective

Clone, push, pull, and inspect remotes.

## Estimated time

30–35 minutes.

## Tasks

Follow the chapter instructions in Zoho Learn and use this folder for practice.

## Submission

Submit the required command output, screenshot, or pull request link in Zoho Learn.

# Question 1: Explain the main difference between a Local Repository and a Remote Repository.
Answer: A Local Repository lives entirely on your physical computer (in the hidden .git folder). It allows you to track changes, create branches, and commit code offline. A Remote Repository is hosted in the cloud on a platform like GitHub. It serves as a centralized, shared backup that allows team members to collaborate, sync, and share their project history.

# Question 2: What is origin in Git, and how is it created?
Answer: origin is the default shorthand alias (or nickname) that Git gives to the URL of the remote repository you connected to your local project. It is automatically created when you run git clone, or it can be manually assigned using the git remote add origin command.

# Question 3: Describe the difference between downloading a repository as a ZIP file vs. cloning it using Git.
Answer:

ZIP Download: Downloads a static, one-time snapshot of the project files. It does not contain the hidden .git directory, meaning you lose the version control history and cannot pull updates or push changes back to the remote repository.

Git Cloning: Downloads the entire working directory plus the complete .git history log. It automatically establishes an active link (origin) back to the remote server, allowing you to seamlessly pull new updates and push your own commits.

# Question 4: What is the relationship between git pull and git push?
Answer: They are exact opposites used to keep your code in sync:

git pull fetches updates from the remote repository (GitHub) and merges them into your local workspace (downloading changes).

git push uploads your local, committed snapshots from your computer up to the remote repository (uploading changes).