#!/usr/bin/env python3

# Dictionary to keep track of food likes
counter = {}

# Open up the favorite foods log and add it to the dictionary
with open("favorite_foods.log", "r") as f:
    for i in f:
        i = i[:-1]
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1

# Sorts the liked foods in descending order
sort_foods = sorted(counter.items(), key = lambda x : x[1], reverse = True)

# Prints out the liked foods
print('Favourite foods, from most popular to least popular')
for i in range(len(sort_foods)):
    print("{}, {}".format(sort_foods[i][0], sort_foods[i][1]))

