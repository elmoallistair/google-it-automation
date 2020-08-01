# Using a Remote Repository

<br>

## What is a remote?

What will happen if the master repository receives a major update since the last local copy was synced?

* Git will push your local copy.
* Nothing will happen.
* **Git will let you know it's time for an update.**
* Git will automatically merge the local copy with the master.

> Great job! If there are pending changes in the master branch, Git will let you know.

<br>

## Video: Working with Remotes

If we want to make a change to a remote branch, what must we do?

* Directly make the change
* Use the git branch -r command
* **Pull the remote branch, merge it with the local branch, then push it back to its origin.**
* Use the git remote -v command

> We still have to go through the normal workflow to change remote branches.

<br>

## Video: Fetching New Changes

What’s the main difference between git fetch and git pull?

* **git fetch fetches remote updates but doesn't merge; git pull fetches remote updates and merges.**
* git pull fetches remote updates but doesn't merge, while git fetch does.
* git fetch clones the entire repository.
* git pull requires a password while git fetch doesn't.

> git pull instantly merges while git fetch only retrieves remote updates.

<br>

## Video: Updating the Local Repository

Assuming no merge conflicts, which type of merge does git pull perform automatically?

* Three-way merge
* Explicit merge
* **Fast-forward merge**
* Half-merge

> As long as there are no conflicts, Git will move the current branch tip up to the target branch tip and combine histories of both commits.