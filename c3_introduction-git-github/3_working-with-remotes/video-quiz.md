## Introduction to Github

<br>

### Video: What is GitHub?

Which BEST describes GitHub?

* A distributed Version Control System (VCS)
* A Software Configuration Management system (SCM)
* **A remote repository hosting service for Git**
* A wiki site for Git users

> GitHub provides free access to a Git server for public and private repositories.

<br>

### Video: Basic Interaction with GitHub

After making changes to our local repository, how do we update the remote repository to reflect our changes?

* Use the git clone command to clone the repository to the server.
* **Use the git push command to send snapshots to the remote repository.**
* Upload a README.md file with Markdown.
* Use the Create a repository form on the website

> The git push command gathers all the snapshots we've taken and sends them to the remote repository.

<br><hr><br>

## Using a Remote Repository

<br>

### What is a remote?

What will happen if the master repository receives a major update since the last local copy was synced?

* Git will push your local copy.
* Nothing will happen.
* **Git will let you know it's time for an update.**
* Git will automatically merge the local copy with the master.

> Great job! If there are pending changes in the master branch, Git will let you know.

<br>

### Video: Working with Remotes

If we want to make a change to a remote branch, what must we do?

* Directly make the change
* Use the git branch -r command
* **Pull the remote branch, merge it with the local branch, then push it back to its origin.**
* Use the git remote -v command

> We still have to go through the normal workflow to change remote branches.

<br>

### Video: Fetching New Changes

What’s the main difference between git fetch and git pull?

* **git fetch fetches remote updates but doesn't merge; git pull fetches remote updates and merges.**
* git pull fetches remote updates but doesn't merge, while git fetch does.
* git fetch clones the entire repository.
* git pull requires a password while git fetch doesn't.

> git pull instantly merges while git fetch only retrieves remote updates.

<br>

### Video: Updating the Local Repository

Assuming no merge conflicts, which type of merge does git pull perform automatically?

* Three-way merge
* Explicit merge
* **Fast-forward merge**
* Half-merge

> As long as there are no conflicts, Git will move the current branch tip up to the target branch tip and combine histories of both commits.

<br><hr><br>

## Solving Conflicts

<br>

### Video: The Pull-Merge-Push Workflow

What should you do with the <<<<<<<, =======, and >>>>>>> conflict markers when resolving a merge conflict?

* **Remove all of the conflict markers and only leave the code as it should be after the merge.**
* Leave the conflict markers surrounding the code that you want to keep.
* Remove the <<<<<<< and >>>>>>> markers, and put the ======= marker in front of the lines that you want to keep.
Do nothing.

> Conflict markers aren’t required when resolving a merge conflict.

<br>

### Video: Pushing Remote Branches

How do you switch to a new local branch?

* **git checkout -b <branch name>**
* git branch b
* git pull origin branch
* git merge branch

> The command git checkout -b <branch name> will first create a new branch and then switch to it.

<br>

### Video: Rebasing Your Changes

What does “git rebase refactor” do?

* **Move the current branch on top of the refactor branch**
* Move the refactor branch on top of the current branch
* Move the refactor branch on top of the master branch
* Move the master branch on top of the refactor branch

> This makes debugging easier and prevents three-way merges by transferring the completed work from one branch to another.

<br>

### Video: Another Rebasing Example

Generally, git rebase is an alternative to which command?

* git fetch
* **git merge**
* git push
* git pull

> Rebasing instead of merging rewrites history and maintains linearity, making for cleaner code.

<br>

### Video: Best Practices for Collaboration

Which of the following statements is true regarding best practices for collaboration?

* Keep the stable version of the project in the master branch, and the latest version on a separate branch.
* Try to fit all changes into one large change.
* You should always rebase changes that have been pushed to a remote repo.
* **Always synchronize your branches before starting any work on your own.**

> This way, when you start changing code, you're starting from the most recent version, minimizing chances of conflicts or the need for rebasing.
