# Solving Conflicts

<br>

## Video: The Pull-Merge-Push Workflow

What should you do with the <<<<<<<, =======, and >>>>>>> conflict markers when resolving a merge conflict?

* **Remove all of the conflict markers and only leave the code as it should be after the merge.**
* Leave the conflict markers surrounding the code that you want to keep.
* Remove the <<<<<<< and >>>>>>> markers, and put the ======= marker in front of the lines that you want to keep.
Do nothing.

> Conflict markers aren’t required when resolving a merge conflict.

<br>

## Video: Pushing Remote Branches

How do you switch to a new local branch?

* **git checkout -b <branch name>**
* git branch b
* git pull origin branch
* git merge branch

> The command git checkout -b <branch name> will first create a new branch and then switch to it.

<br>

## Video: Rebasing Your Changes

What does “git rebase refactor” do?

* **Move the current branch on top of the refactor branch**
* Move the refactor branch on top of the current branch
* Move the refactor branch on top of the master branch
* Move the master branch on top of the refactor branch

> This makes debugging easier and prevents three-way merges by transferring the completed work from one branch to another.

<br>

## Video: Another Rebasing Example

Generally, git rebase is an alternative to which command?

* git fetch
* **git merge**
* git push
* git pull

> Rebasing instead of merging rewrites history and maintains linearity, making for cleaner code.

<br>

## Video: Best Practices for Collaboration

Which of the following statements is true regarding best practices for collaboration?

* **Keep the stable version of the project in the master branch, and the latest version on a separate branch.**
* Try to fit all changes into one large change.
* You should always rebase changes that have been pushed to a remote repo.
* Always synchronize your branches before starting any work on your own.

> This way, when you start changing code, you're starting from the most recent version, minimizing chances of conflicts or the need for rebasing.