# Branching and Merging

<br>

## Video: What is a branch? 

What is the purpose of organizing repositories into branches?

* To enable changes to be worked on without disrupting the most current working state.
* To make it easier to undo commits.
* To enable changes to the repository to permanently replace previous commits.
* To give users a place to keep notes.

> By creating a new branch, we can experiment without breaking what already works.

<br>

## Video: Creating New Branches

What does the ***git checkout -b new branch*** command do?

* Switches to another branch and immediately commits.
* Checks if the new branch is ahead of the main branch.
* Merges two branches.
* Creates a new branch and switches to it.

<br>

## Video: Working with Branches

How does ***git checkout*** switch branches?

* By creating a new commit on a new branch.
* **By updating the working tree to match the selected branch.**
* By moving the HEAD to the previous commit.
* By amending the commit with the provided ID.

> The HEAD is moved to the relevant commit on the specified branch.

<br>

## Video: Merging

What happens when we merge two branches?

* The HEAD points at the master branch.
* **Both branches are pointed at the same commit.**
* One of the former branches disappears.
* Two independent snapshots will now share the same name.

> Merging combines branched data and history together.

<br>

## Video: Merge Conflicts

What's the advantage of Git throwing a merge conflict error in cases of overlap?

* **It prevents loss of work if two lines overlap.**
* It helps us understand which changes to keep.
* It warns us of all potential problems.
* It tells us whether the commit is a merge

> If two lines have differences Git is unsure about, it's best we decide than risk losing work forever.