# Video: The Pull-Merge-Push Workflow
atom all_checks.py # modify file
git add -p
git commit -m "Rename min_absolute to min_gb, use parameter names"
git push # fails, reason: the remote repository contains changes that we don't have in our local branch
git pull # sync local remote with the remote repository
         # merge conflict in all_checks.py
atom all_checks # fix conflict
git add all_checks.py
git commit
git push

# Video: Pushing Remote Branches
git checkout -b refactor # create and switch to new branch 
atom all_checks.py # modify
git commit -a -m "Create wrapper function for check_disk_full"
./all_checks.py # test code
git commit -a -m "Iterate over a list of checks and message to avoid code duplcation"
./all_checks.py # test code
git commit -a -m "Allow printing more than one error message"
git push -u origin refactor # push a branch to a remote repo