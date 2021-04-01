#/usr/bin/bash

# Video: Skipping the Staging Area
cd scripts
atom all_checks.py # modify file
git commit -a -m "Call check_reboot from main, exit with 1 on error" # A shortcut to stage any changes to tracked files and commit them in one step
git log # head indicator has now moved to the latest commit

# Video: Getting More Information About Our Changes
git log -p # gives us the patch that was created
git show <commit-id> # see a specific commit
git --stat # show stats about the changes in the commit, like whick file were changed and how many lines were added/removed
git diff --staged # see the changes that are staged but not commited

# Video: Deleting and Renaming Files
cd checks
git rm process.py # delete file from repository
git status # out: 'deleted: process.py'
git mv disk_usage.py check_free_space.py # rename file
git status # out: 'renamed: mv disk_usage.py -> check_free_space.py'
git commit -m "New name for disk_usage"
echo .DS_STORE > .gitignore # create .gitignore file
git add .gitignore
git commit -m "Add a gitignore file, ignoring .DS_STORE files"