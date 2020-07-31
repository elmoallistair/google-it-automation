#/usr/bin/bash

# Video: First Steps with Git
git config --global user.email "me@example.com"
git config --global user.name "My name"
git init # initialize an empty git repository
git add .
git status
git commit

# Video: Tracking Files
atom disk_usage.py # modify file
git add disk_usage.py
git status # out: modified: disk_usage.py
git commit -m "Add periods to the end of sentences"
git status # out: nothing to commit, working tree clean

# Video: The Basic Git Workflow
mkdir scripts
cd scripts
git init # initialize an empty git repository
git config -l # check current configuration
atom all_checks.py # create file
chmod +x all_checks.py
git status # out: untracked files: all_checks.py
git add all_checks.py
git commit -m "Create an empty all_checks.py"
atom all_checks.py # modify file
git status # out: changes not staged for commit: all_checks.py
git add all_checks.py
git status # out: changes to be commited: all_checks.py
git commit -m "Add a check_reboot function"

# Video: Anatomy of a Commit Message
cat example_commit.txt
cd scripts
git log # check history of commit