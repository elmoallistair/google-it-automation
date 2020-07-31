#!/usr/bin/env python3

# Dictionary to keep track of food likes
counter = {}

# Open up the favorite foods log and count frequencies using the dictionary
with open("favorite_foods.log", "r") as f:
    for line in f:
        item = line.strip()
        if item not in counter:
            counter[item] = 1
        else:
            counter[item] += 1

# Print out all the available liked foods
print("Select your favorite food below:")
for item in counter:
    print(item)

# Ask which food is the user's favorite
answer = input("Which of the foods above is your favorite? ")
answer = answer.lower()

# Print out how many others like the user's favorite food, otherwise say it can't be found
try:
    print("{} of your friends like {} as well!".format(counter[answer], answer))
    exit(0)
except KeyError:
    print("Hmm we couldn't find anyone who also likes \"{}\".".format(answer))
    print("Did you enter one of the foods listed above?")
    exit(0)
