## Advanced Git Interaction

<br>

### Video: Skipping the Staging Area

If we're making a small change and want to skip the staging step, which two flags do we need to add to the git commit command? Check all that apply.

* **-m**
* -t
* -l
* **-a**

> The -m flag allows us to directly add the commit message to the command.

> The -a flag lets us add and commit in the same step.

<br>

### Video: Getting More Information About Our Changes

If we want to see a specific commit, which command would we use along with the commit ID?

* git log --stat
* **git show**
* git log -p
* git commit -am 

> Taking the commit ID, git show will show information about the commit and its associated patch.

<br>

### Video: Deleting and Renaming Files

If we need to delete a file from our repository, we'll need to run a command to delete the file and then stage and commit the change. Which command would we use to delete the file?

* **git rm**
* git mv
* git diff
* git del

> This command removes files from the working tree and from the index.

<br><br>

## Undoing Things

<br>

### Video: Undoing Changes Before Committing

What is the purpose of the git checkout command?

* It finalizes staged changes.
* **It reverts changes to modified files before they are staged.**
* It skips staging and directly commits.
* It displays the current status of the commit.

> git checkout restores files to the latest stored snapshot, reverting any changes before staging.

<br>

### Video: Amending Commits

What does the ***git commit --amend*** do?

* Add an error log to the commit.
* Remove files from the staging area.
* Change the commit message.
* **Overwrite the previous commit.**

> ***git commit --amend*** allows us to modify and add changes to the most recent commit. 

<br>

### Video: Rollbacks

Which of the following is true about the ***git revert*** command?

* It undoes a commit as though it never happened.
* **It creates a new commit with inverse changes**.
* The output of ***git revert*** is not the same as a regular commit.
* It does not include the ID of the commit that was reverted.

> With ***git revert***, a new commit is created with inverse changes. This cancels previous changes instead of making it as though the original commit never happened.

<br>

### Video: Identifying a Commit

Which of the following is NOT true about the SHA1 hash numbers that Git uses to identify commits?

* They provide the consistency that is critical for distributed systems such as Git.
* They are created using the commit message, date, author, and the snapshot taken of the working tree.
* **Git requires the entire hash ID to identify a commit.**
* They are composed of 40 characters.

> Git can identify a commit using the first few hash numbers as long as there is only one matching possibility.

<br><br>

## Branching and Merging

<br>

### Video: What is a branch? 

What is the purpose of organizing repositories into branches?

* To enable changes to be worked on without disrupting the most current working state.
* To make it easier to undo commits.
* To enable changes to the repository to permanently replace previous commits.
* To give users a place to keep notes.

> By creating a new branch, we can experiment without breaking what already works.

<br>

### Video: Creating New Branches

What does the ***git checkout -b new branch*** command do?

* Switches to another branch and immediately commits.
* Checks if the new branch is ahead of the main branch.
* Merges two branches.
* Creates a new branch and switches to it.

<br>

### Video: Working with Branches

How does ***git checkout*** switch branches?

* By creating a new commit on a new branch.
* **By updating the working tree to match the selected branch.**
* By moving the HEAD to the previous commit.
* By amending the commit with the provided ID.

> The HEAD is moved to the relevant commit on the specified branch.

<br>

### Video: Merging

What happens when we merge two branches?

* The HEAD points at the master branch.
* **Both branches are pointed at the same commit.**
* One of the former branches disappears.
* Two independent snapshots will now share the same name.

> Merging combines branched data and history together.

<br>

### Video: Merge Conflicts

What's the advantage of Git throwing a merge conflict error in cases of overlap?

* **It prevents loss of work if two lines overlap.**
* It helps us understand which changes to keep.
* It warns us of all potential problems.
* It tells us whether the commit is a merge

> If two lines have differences Git is unsure about, it's best we decide than risk losing work forever.