# Expressions and Variables

<br>

## Video: Data Types

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

## Video: Variables

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

## Video: Expressions, Numbers, and Type Conversions

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