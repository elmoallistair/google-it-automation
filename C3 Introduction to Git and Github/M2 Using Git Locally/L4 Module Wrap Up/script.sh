# Explore repository
cat favorite_foods.log
./food_count.py
./food_question.py
git config user.name "Name"
git config user.email "user@example.com"

# Understanding the repository
git status
git log
git config user.name "Name"
git config user.email "user@example.com"

# Add a new feature
git branch improve-output
git checkout improve-output
echo "print('Favourite foods, from most popular to least popular')" >> food_count.py
./food_count.py
git add food_count.py
git commit -m "Adding a line in the output describing the utility of food_count.py script"

# Fix the script
./food_question.py
git log
git revert [commit-ID]
./food_question.py

# Merge operation
git checkout master
git merge improve-output
./food_question.py
git status
git log
