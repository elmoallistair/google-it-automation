# Using Git

<br>

## Video: First Steps with Git

What are the git directory and the working tree?

* The git directory stores configuration settings and the working tree stores the history of the files.
* The git directory is copied to the computer and the working tree stays in the remote repository.
* The git directory is a sandbox for changing the files and the working tree contains old versions of the files.
* **The git directory contains all the changes and their history and the working tree contains the current versions of the files.**

> The git directory acts as a database for all the changes tracked in Git and the working tree acts as a sandbox where we can edit the current versions of the files.

<br>

## Video: Tracking Files

What do we need to do after modifying a file tracked by Git?

* **We need to stage the file, so that the changes will be included in the next commit.**
* We need to commit the file, so that the changes will become part of the staging area.
* We need to add the file to the Git directory.
* We need to change to a different working tree.

> After modifying a file, we need to stage those changes and then commit them afterwards.

<br>

## Video: The Basic Git Workflow

When committing new files or changes with git commit, the user is asked to provide a commit message. What will happen if an empty commit message is entered?

* It will make it difficult to track bugs without commit messages.
* The info shown with the git log command will show no commit message.
* The commit will be aborted.
* The commit will ignore untracked files or files that weren't staged.

> You can’t commit with an empty commit message.

<br>

## Video: Anatomy of a Commit Message

What should your commit message look like?

* A jumble of words
* A description of no more than 50 characters
* **A short description of the change (up to 50 characters), followed by one or more paragraphs giving more details of the change (if needed).**
* Always write as much as you can about the changes.

> You want your message to contain all relevant information without being confusing.