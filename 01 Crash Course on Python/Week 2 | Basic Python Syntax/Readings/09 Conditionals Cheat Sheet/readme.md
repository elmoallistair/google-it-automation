## Conditionals Cheat Sheet

<hr>

**Conditionals Cheat Sheet**

In earlier videos, we took a look at some of the built-in Python operators that allow us to compare values, and some logical operators we can use to combine values. We also learned how to use operators in if-else-elif blocks. 

It’s a lot to learn but, with practice, it gets easier to remember it all. In the meantime, this handy cheat sheet gives you all the information you need at a glance. 

Comparison operators
* a == b: a is equal to b
* a != b: a is different than b
* a < b: a is smaller than b
* a <= b: a is smaller or equal to b
* a > b: a is bigger than b
* a >= b: a is bigger or equal to b

Logical operators
* a and b: True if both a and b are True. False otherwise.
* a or b: True if either a or b or both are True. False if both are False.
* not a: True if a is False, False if a is True.

**Branching blocks**

In Python, we branch our code using if, else and elif. This is the branching syntax:

```
if condition1:
	if-block
elif condition2:
	elif-block
else:
	else-block
```

Remember: The if-block will be executed if condition1 is True. The elif-block will be executed if condition1 is False and condition2 is True. The else block will be executed when all the specified conditions are false.