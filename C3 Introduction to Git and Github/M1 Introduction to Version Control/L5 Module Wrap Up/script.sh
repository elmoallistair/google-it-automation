#/usr/bin/bash

# Install Git
sudo apt update
sudo apt install git
git --version

# Initialize a new repository
mkdir my-git-repo
cd my-git-repo
git init

# Configure Git
git config --global user.name "Name"
git config --global user.email "user@example.com"

# Git Operations
echo "This is my first repository." > readme
git add README
git commit -m "This is my first commit!"
echo "A repository is a location where all the files of a particular project are stored." > readme
git diff README
git add README
git status
git commit -m "This is my second commit."
git log
