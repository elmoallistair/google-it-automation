## Practice Quiz: Undoing Things
* **Total points: 5**
* **Score: 100%**

<br>

### Question 1

Let's say we've made a mistake in our latest commit to a public branch. Which of the following commands is the best option for fixing our mistake?

* **git revert**
* git commit --amend
* git reset
* git checkout -- <file>

> git revert will create a new commit to reverse the previous one, and is the best option for undoing commits on public branches.

<br>

### Question 2

If we want to rollback a commit on a public branch that wasn't the most recent one using the revert command, what must we do?

* Use the git reset HEAD~2 command instead of revert
* Use the revert command repeatedly until we've reached the one we want
* **Use the commit ID at the end of the git revert command**
* Use the git commit --amend command instead

> The commit ID is a 40-character hash that identifies each commit.

<br>

### Question 3

What does Git use cryptographic hash keys for?

* To secure project backups
* **To guarantee the consistency of our repository**
* To encrypt passwords
* To identify commits

> Git doesn't really use these hashes for security. Instead, they’re used to guarantee the consistency of our repository.

<br>

### Question 4

What does the command git commit --amend do?

* Start a new branch
* Create a copy of the previous commit
* Delete the previous commit
* **Overwrite the previous commit**

> The command git commit --amend will overwrite the previous commit with what is already in the staging area.

<br>

### Question 5

How can we easily view the log message and diff output the last commit if we don't know the commit ID?

* **git show**
* git identify
* git log
* git revert

> The git show command without an object parameter specified  will default to show us information about the commit pointed to by the HEAD.