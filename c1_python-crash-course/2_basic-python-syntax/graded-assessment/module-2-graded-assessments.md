## Module 2 Graded Assessment
* **Total points: 10**
* **Grade: 100%**

<br>

#### Question 1

Complete the function by filling in the missing parts. The color_translator function receives the name of a color, then prints its hexadecimal value. Currently, it only supports the three additive primary colors (red, green, blue), so it returns "unknown" for all other colors.

```
def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color
	
print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown
```

Output:

```
#0000ff
unknown
#ff0000
unknown
#00ff00
unknown
```

<br>

#### Question 2

What's the value of this Python expression: "big" > "small"
* True
* **False**
* big
* small

> The conditional operator > checks if two values are equal. The result of that operation is a boolean: either True or False. Alphabetically, "big" is less than "small".

<br>

### Question 3

What is the elif keyword used for?
* To mark the end of the if statement
* **To handle more than two comparison cases**
* To replace the "or" clause in the if statement
* Nothing - it's a misspelling of the else-if keyword

> The elif keyword is used in place of multiple embedded if clauses, when a single if/else structure is not enough.

<br>

### Question 4

Students in a class receive their grades as Pass/Fail. Scores of 60 or more (out of 100) mean that the grade is "Pass". For lower scores, the grade is "Fail". In addition, scores above 95 (not included) are graded as "Top Score". Fill in this function so that it returns the proper grade.

```
def exam_grade(score):
	if score > 95:
		grade = "Top Score"
	elif score >= 60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail
```

Output:

```
Pass
Fail
Pass
Pass
Top Score
Fail
```

<br>

### Question 5

What's the value of this Python expression: `11 % 5`?
* 2.2
* 2
* **1**
* 0

> "%" is the modulo operator, which returns the remainder of the integer division between two numbers. 11 divided by 5 equals 2 with remainder of 1.

<br>

### Question 6

Complete the body of the ***format_name*** function. This function receives the ***first_name*** and ***last_name*** parameters and then returns a properly formatted string.

Specifically:

* If both the ***last_name*** and the ***first_name*** parameters are supplied, the function should return like so:
* If only one name parameter is supplied (either the first name or the last name)
* Finally, if both names are blank, the function should return the empty string

```
def format_name(first_name, last_name):
	# code goes here
	string = 'Name: ' + ', '.join([name for name in [last_name, first_name] if name]) if any([last_name, first_name]) else ''
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
```

Output:

```
Name: Hemingway, Ernest
Name: Madonna
Name: Voltaire
```

<br>

### Question 7

The longest_word function is used to compare 3 words. It should return the word with the most number of characters (and the first in the list when they have the same length). Fill in the blank to make this happen.

```
def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))
```

Output:

```
chair
beyond
notebook

```

<br>

### Question 8

What’s the output of this code?

```
def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))
```

Output:

```
10
```

<br>

### Question 9

What's the value of this Python expression?

`((10 >= 5*2) and (10 <= 5*2))`

* **True**
* False
* 10
* 5*2

> When using the "and" operator, a statement is True if both parts of the conditional are True

<br>

### Question 10

The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1). Complete the body of the function so that it returns the right number. Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.

```
def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
	# keep just the fractional part of the quotient
	return (numerator / denominator) % 1 if denominator else 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
```

Output:

```
0.0
0.25
0.6666666666666667
0.5
0
0.0
```