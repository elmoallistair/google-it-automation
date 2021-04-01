# Video: Working with Remotes
git remote -v # check configuration of remote
git remote show origin # get more information about our remote
git branch -r # look at the remote branch that our Git repo is currently tracking
git status # tells us that our branch is up to date with the origin/master branch

# Video: Fetching New Changes
git fetch # copies the commits done in the remote repository to the remote branches

# Video: Updating the Local Repository
git pull # fetch the remote copy of the current branch and automatically try to merge it
git remote show origin
git checkout experimental # create a local branch
git remote update # fetch the contents of all remote branches