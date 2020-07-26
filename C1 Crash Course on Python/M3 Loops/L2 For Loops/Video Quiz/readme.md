# For Loops

<br>

## Video: What is a for loop?

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

## Video: More for Loop Examples

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

## Video: Nested for Loops

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

## Video: Common Errors in for Loops

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