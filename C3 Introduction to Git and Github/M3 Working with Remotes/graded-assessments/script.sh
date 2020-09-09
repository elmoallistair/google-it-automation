#/usr/bin/bash

# Git operations

git clone [URL]
git clone https://github.com/[username]/[git-repo].git
cd [directory_name]

# Configure Git
git config --global user.name "Name"
git config --global user.email "user@example.com"

# Edit the file and add it to the repository
nano README.md
I am editing the README file. Adding some more details about the project description.
git status
git add README.md
git commit
I am editing the README file.
git push origin master

# Create a new file and commit it to the repository
nano example.py
git add example.py
git commit

# Add an empty file to the repository through web UI
git push origin master # error
git pull origin master
git push origin master
