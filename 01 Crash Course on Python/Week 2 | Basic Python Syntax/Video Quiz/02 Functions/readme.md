# Functions

## Defining Functions

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

## Returning Values

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

## The Principles of Code Reuse

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

## Code Style

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