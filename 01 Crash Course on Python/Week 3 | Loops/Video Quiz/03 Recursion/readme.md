# Recursion

## What is recursion? (Optional)

The function sum_positive_numbers should return the sum of all positive numbers between the number n received and 1. For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15. Fill in the gaps to make this work:

```
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15
```

Output:

```
6
15
```

## Recursion in Action in the IT Context

Which of the following scenarios would benefit the most from using a recursive function to solve the problem?

* You need to print out a list of the employees in your company.
* You need to know how many files are present in a single directory of your computer.
* **You need to create a family tree, showing several generations of your ancestors, with all of their children.**
* You need to calculate the square root of numbers 1 through 10.

> It's a better solution than the traditional looping techniques