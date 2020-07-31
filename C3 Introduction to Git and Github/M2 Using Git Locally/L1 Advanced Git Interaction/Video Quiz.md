# Advanced Git Interaction

<br>

## Video: Skipping the Staging Area

If we're making a small change and want to skip the staging step, which two flags do we need to add to the git commit command? Check all that apply.

* **-m**
* -t
* -l
* **-a**

> The -m flag allows us to directly add the commit message to the command.

> The -a flag lets us add and commit in the same step.

<br>

## Video: Getting More Information About Our Changes

If we want to see a specific commit, which command would we use along with the commit ID?

* git log --stat
* **git show**
* git log -p
* git commit -am 

> Taking the commit ID, git show will show information about the commit and its associated patch.

<br>

## Video: Deleting and Renaming Files

If we need to delete a file from our repository, we'll need to run a command to delete the file and then stage and commit the change. Which command would we use to delete the file?

* **git rm**
* git mv
* git diff
* git del

> This command removes files from the working tree and from the index.

<br>