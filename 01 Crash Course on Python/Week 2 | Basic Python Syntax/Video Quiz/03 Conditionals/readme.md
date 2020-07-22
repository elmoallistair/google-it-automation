# Conditionals

## Comparing Things

Figure out what's the relationship between the strings "cat" and "Cat" by replacing the plus sign with comparison operators.

```
print("cat" > "Cat")
```

* "cat" equals "Cat"
* "cat" is smaller than "Cat"
* **"cat" is larger than "Cat"**

* In Python uppercase letters are alphabetically sorted before lowercase letters.

## Branching with if Statements

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

## else Statements

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

## elif Statements

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