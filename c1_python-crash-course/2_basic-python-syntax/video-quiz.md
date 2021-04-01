## Expressions and Variables

<br>

### Video: Data Types

Why does this code raise an error:

```
print("1234"+5678)
```

* **Because Python doesn't know how to add a number to a string.**
* Because in Python it's only possible to add numbers, not strings.
* Because in Python it's not possible to print integers.
* Because numbers shouldn't be written between quotes.

> Python can add a number to a number or a string to a string, but it doesn't know how to add a number to a string.

<br>

### Video: Variables

Fill in the blanks to calculate the area of a triangle of base 5, height 3 and output the result. **Reminder**: the area of a triangle is (base*height)/2.

```
base = 5
height = 3
area = (base*height)/2

print(area)
```

Output:

```
7.5
```

<br>

### Video: Expressions, Numbers, and Type Conversions

In this scenario, we have a directory with 5 files in it. Each file has a different size: 2048, 4357, 97658, 125, and 8. Fill in the blanks to calculate the average file size by having Python add all the values for you, and then set the files variable to the number of files. Finally, output a message saying "The average size is: " followed by the resulting number. Remember to use the str() function to convert the number into a string. 

```
total = 2048 + 4357 + 97658 + 125 + 8
files =5
average = total / files
print("The average size is: " + str(average))
```

Output:

```
The average size is: 20839.2
```

<br><hr><br>

## Functions

<br>

### Video: Defining Functions

Flesh out the body of the print_seconds function so that it prints the total amount of seconds given the hours, minutes, and seconds function parameters. Remember that there are 3600 seconds in an hour and 60 seconds in a minute.

```
def print_seconds(hours, minutes, seconds):
    print(hours*3600 + minutes*60 + seconds)

print_seconds(1,2,3)
```

Output:

```
3723
```

<br>

### Video: Returning Values

Use the get_seconds function to work out the amount of seconds in 2 hours and 30 minutes, then add this number to the amount of seconds in 45 minutes and 15 seconds. Then print the result.

```
def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)
```

Output:

```
11715
```

<br>

### Video: The Principles of Code Reuse

In this code, identify the repeated pattern and replace it with a function called month_days, that receives the name of the month and the number of days in that month as parameters. Adapt the rest of the code so that the result is the same. Confirm your results by making a function call with the correct parameters for both months listed.

```
def month_days(month, days):
    return f"{month} has {days} days."
    
print (month_days("June", 30))
print (month_days("July", 31))
```

Output:

```
June has 30 days.
July has 31 days.
```

<br>

### Video: Code Style

This function to calculate the area of a rectangle is not very readable. Can you refactor it, and then call the function to calculate the area with base of 5 and height of 6? Tip: a function that calculates the area of a rectangle should probably be called rectangle_area, and if it's receiving base and height, that's what the parameters should be called.

```
def rectangle_area(base, height):
	area = base * height
	return "The area is " + str(area)
	
print(rectangle_area(10, 5))
```

Output:

```
The area is 50
```

<br><hr><br>

## Conditionals

<br>

### Video: Comparing Things

Figure out what's the relationship between the strings "cat" and "Cat" by replacing the plus sign with comparison operators.

```
print("cat" > "Cat")
```

* "cat" equals "Cat"
* "cat" is smaller than "Cat"
* **"cat" is larger than "Cat"**

* In Python uppercase letters are alphabetically sorted before lowercase letters.

<br>

### Video: Branching with if Statements

The is_positive function should return True if the number received is positive, otherwise it returns None. Can you fill in the gaps to make that happen?

```
def is_positive(number):
  if number > 0:
    return True
  return None
```

Output:

```
is_positive(-5) returned None
is_positive(0) returned None
is_positive(13) returned True
```

<br>

### Video: else Statements

The is_positive function should return True if the number received is positive and False if it isn't. Can you fill in the gaps to make that happen?

```
def is_positive(number):
  if number > 0:
    return True
  else:
    return False
```

Output:

```
is_positive(-5) returned False
is_positive(0) returned False
is_positive(13) returned True
```

<br>

### Video: elif Statements

The number_group function should return "Positive" if the number received is positive, "Negative" if it's negative, and "Zero" if it's 0. Can you fill in the gaps to make that happen?

```
def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative
```

Output:

```
Positive
Zero
Negative
```