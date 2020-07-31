#/usr/bin/bash

# Video: Creating New Branches
cd checks
git branch # show list all branches in repository
git branch new-feature # create new branch: new-feature
git checkout new-feature # switch to new-feature branch
git checkout -b even-better-feature # Creates a new branch and switches to it
atom free_memory.py
git add free_memory.py
git commit -m "Add an empty free_memory.py"

# Video: Working with Branches
cd checks
git status # out: working tree clean 
ls -l # out: disk_usage.py; free_memory.py
git checkout master
git log -2 # recent commit of the master branch
ls -l # out: disk_usage.py
git branch -d new-feature # delete branch: new-feature

# Video: Merging
git merge even-better-feature # merge the even-better-feature branch into the master branch (fast-forward merge)

# Video: Merge Conflicts
atom free_memory.py # modify file
git commit -a -m "Add comment to main()"
git checkout even-better-feature # switch branch
atom free_memory.py # modify file
git commit -a -m "Print everthing ok"
git checkout master # switch to master branch
git merge even-better-feature # out: merge conflic in free_memory.py
git status # get information
atom free_memory.py # fix conflict by deleting
git add free_memory.py
git status # out: all conflicts fixed
git log --graph --oneline