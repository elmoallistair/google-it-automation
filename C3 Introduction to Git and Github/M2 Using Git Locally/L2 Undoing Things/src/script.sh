#/usr/bin/bash

# Video: Undoing Changes Before Comitting
cd scripts
atom all_checks.py # modify file
./all_checks # broken script
git checkout all_checks.py # discard changes in working directory
git status
./all_checks # still error
atom all_checks.py # fix
./all_checks # done
./all_checks.py > output.txt # create temporary file with the output of all_checks.py script
git add * # add all unstaged changes in working tree
git status # out: `modified: all_checks.py; new_file: output.txt`
git reset HEAD output.txt 
git status # out: `modified: all_checks.py; untracked file: output.txt`
git commit -m "it should be os.path.exists" # commit fixed typo

## Amending Commits
cd scripts
touch auto-update.py
touch gather-information.sh
git add auto-update.py # add 1 file
git commit -m "Add two new scripts" # wrongs commit msg
git add gather-information.sh
git commit --ammend # add a line of description in editor

# Video: Rollbacks

cd scripts
atom all_checks.py # modify file
git commit -a -m "Add call to disk_full function"
./all_checks.py # error
git revert # add explanation why we do rollback: 'the disk_full function is undefined'
git log -p -2