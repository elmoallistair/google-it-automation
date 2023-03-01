## While Loops

<br>

### Video: What is a while loop?

```
x = 0
while x < 5:
  print("Not there yet, x=" + str(x))
  x = x + 1
print("x=" + str(x))
```

How many times will "Not there yet" be printed?

> 5

<br>

### Video: More while Loop Examples

Can you work out what this function does? Try passing different parameters to the attempts function to see what it does. 

```
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(3)
```

Output:

```
Attempt 1
Attempt 2
Attempt 3
Done
```

<br>

### Video: Why Initializing Variables Matters

In this code, there's an initialization problem that's causing our function to behave incorrectly. Can you find the problem and fix it?

```
def count_down(start_number):
  current = start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)
```

Output:

```
3
2
1
Zero!
```

<br>

### Video: Infinite Loops and How to Break Them

The following code causes an infinite loop. Can you figure out what’s missing and how to fix it?

```
def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
        	n += 1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 
```

Output:

```
1
2
3
4
5
```

<br><hr><br>

# For Loops

<br>

### Video: What is a for loop?

Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares of numbers between 0 and x (not included). Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (not included).

```
def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285
```

Output:

```
285
```

<br>

### Video: More for Loop Examples

In math, the factorial of a number is defined as the product of an integer and all the integers below it. For example, the factorial of four (4!) is equal to 1\*2\*3\*4=24. Fill in the blanks to make the factorial function return the right number.

```
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120
```

Output:

```
24
120
```

<br>

### Video: Nested for Loops

Given the following code:

```
teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
```

What should the next line be to avoid both variables being printed with the same value?

* while home_team != away_team:
* for home_team == away_team:
* away_team = home_team
* **if home_team != away_team:**

> We want to print all possible team pairings but exclude those where a team would play against itself. To do that, we need a conditional that skips the case where both teams are the same.

<br>

### Video: Common Errors in for Loops

The validate_users function is used by the system to check if a list of users is valid or invalid. A valid user is one that is at least 3 characters long. For example, ['taylor', 'luisa', 'jamaal'] are all valid users. When calling it like in this example, something is not right. Can you figure out what to fix?

```
def validate_users(users):
  if len(users) > 3:
    print(users + " is valid")
  else:
    print(users + " is invalid")

validate_users("purplecat")
```

Output:

```
purplecat is valid
```

# Recursion

<br>

### Video: What is recursion? (Optional)

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

<br>

### Video: Recursion in Action in the IT Context

Which of the following scenarios would benefit the most from using a recursive function to solve the problem?

* You need to print out a list of the employees in your company.
* You need to know how many files are present in a single directory of your computer.
* **You need to create a family tree, showing several generations of your ancestors, with all of their children.**
* You need to calculate the square root of numbers 1 through 10.

> It's a better solution than the traditional looping techniques
