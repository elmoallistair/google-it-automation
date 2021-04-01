## Before Version Control

<br>

### Video: Keeping Historical Copies

What’s the goal of a version control system?

* To make sure that our code has no bugs
* **To keep track of changes made to our files**
* To have backup copies of our code
* To store code, images, configuration, and videos

> A version control system allows us to keep track of when and who did what changes to our files. Those can be code, configuration, images, or whatever else we need to track.

<br>

### Video: Diffing Files

What’s the goal of the diff tool?

* To keep track of changes to our files
* To check if our changes make sense
* To highlight new lines in Python files
* **To show the differences between two files**

> The diff tool shows all the differences between any type of file. By highlighting what’s changed, it helps us understand the changes and see how the files have been modified.

<br>

### Video: Applying Changes

What does the patch command do?

* It generates a file with the differences between two files.
* It shows the changes made in a directory of files.
* It redirects the contents of a file into standard input.
* **It applies the changes contained in a diff file to another file.**

> While diff is the command that generates the difference between two files, patch is the command that applies those differences to the original file.

<br>

### Video: Practical Application of diff and patch

We've prepared a diff file with the changes that need to be applied to the script. What does our colleague need to do now?

* Look at the changes in the diff file and manually modify the original file with those same changes.
* Run diff disk_usage.diff disk_usage.py.
* Ask us to send them the full file, not just the diff file.
* **Run patch disk_usage.py < disk_usage.diff.**

> To automatically apply changes to a file, we need to run the patch command on the file that we want to modify with the diff file as input.

<br><hr><br>

## Version Control System

<br>

### Video: What is version control?

What does a version control system do?

* It groups all related code.
* It explains why a change was made.
* **It keeps track of changes we do to our files.**
* It prevents us from changing files by mistake.

> By keeping track of the changes that we make to our files, a VCS lets us know when a file changed, who changed it, and also lets us easily roll back those changes.

<br>

### Video: Version Control and Automation

Why is a version control system useful, even if it's used only by a single person? Check all that apply.

* **Seeing the history of the changes helps us understand what changed and why.**
* Tracking code in a VCS ensures that it's bug free.
* **Tracking changes allows for easy rollbacks when a problem is detected.**
* Storing files in a VCS avoids the need for any kind of backups.

> One of the main benefits of a VCS is that you can see the history of how files changed and understand what changed at each step and what motivated the change.

> By having each change tracked in the VCS, it's very easy to go back to previous versions when an issue with a change is discovered.

<br>

### Video: What is Git?

What characteristics make Git particularly powerful? Check all that apply.

* It was created by Linus Torvalds in 2005.
* **It's a distributed VCS, which means that each developer has a full copy of the repository.**
* It's maintained by a team of distributed developers.
* **Repositories can be used by as many developers as needed.**

> Because each contributor to a Git repo has a full copy of the repository, they can interact with the tracked files without needing a coordinating server. In turn, this improves collaboration.

> Because of the way Git was designed, repositories can be useful for any number of developers, from one to thousands.

<br>

### Video: Installing git

What’s the command that you need to run to check what version of Git is currently installed in your computer?

* git init
* git show version
* git commit
* **git --version**

> Running git --version in your computer will display the currently installed version of Git (if Git is installed on your computer).

<br><hr><br>

## Using Git

<br>

### Video: First Steps with Git

What are the git directory and the working tree?

* The git directory stores configuration settings and the working tree stores the history of the files.
* The git directory is copied to the computer and the working tree stays in the remote repository.
* The git directory is a sandbox for changing the files and the working tree contains old versions of the files.
* **The git directory contains all the changes and their history and the working tree contains the current versions of the files.**

> The git directory acts as a database for all the changes tracked in Git and the working tree acts as a sandbox where we can edit the current versions of the files.

<br>

### Video: Tracking Files

What do we need to do after modifying a file tracked by Git?

* **We need to stage the file, so that the changes will be included in the next commit.**
* We need to commit the file, so that the changes will become part of the staging area.
* We need to add the file to the Git directory.
* We need to change to a different working tree.

> After modifying a file, we need to stage those changes and then commit them afterwards.

<br>

### Video: The Basic Git Workflow

When committing new files or changes with git commit, the user is asked to provide a commit message. What will happen if an empty commit message is entered?

* It will make it difficult to track bugs without commit messages.
* The info shown with the git log command will show no commit message.
* The commit will be aborted.
* The commit will ignore untracked files or files that weren't staged.

> You can’t commit with an empty commit message.

<br>

### Video: Anatomy of a Commit Message

What should your commit message look like?

* A jumble of words
* A description of no more than 50 characters
* **A short description of the change (up to 50 characters), followed by one or more paragraphs giving more details of the change (if needed).**
* Always write as much as you can about the changes.

> You want your message to contain all relevant information without being confusing.