## Practice Quiz: Advanced Git Interaction
* **Total points: 5**
* **Score: 100%**

<br>

### Question 1

Which of the following commands is NOT an example of a method for comparing or reviewing the changes made to a file?

* git log -p
* git diff --staged
* git add -p
* **git mv**

> git mv won't give you any information on changes. Instead, it is used to move or rename a file or directory in Git.

<br>

### Question 2

What is the gitignore file?

* A file containing a list of commands that Git will ignore.
* A file the user is intended to ignore.
* A file listing uncommitted changes.
* **A file containing a list of files or filename patterns for Git to skip for the current repo.**

> The gitignore file is a text file that tells Git which files or folders to ignore in a project.

<br>

### Question 3

What kind of file will the command git commit -a not commit?

* Tracked files
* **New files**
* Old files
* Staged files

> Files that are new and untracked will not be committed before being added.

<br>

### Question 4

What does HEAD represent in Git?

* The subject line of a commit message
* The top portion of a commit
* **The currently checked-out snapshot of your project**
* The first commit of your project

> In all cases, HEAD is used to indicate what the currently checked-out snapshot is.

<br>

### Question 5

If we want to show some stats about the changes in a commit, like which files were changed and how many lines were added or removed, what flag should we add to git log?

* **--stat**
* --patch
* -2
* --pretty

> This will cause git log to show some stats about the changes in the commit, like which files were changed and how many lines were added or removed.