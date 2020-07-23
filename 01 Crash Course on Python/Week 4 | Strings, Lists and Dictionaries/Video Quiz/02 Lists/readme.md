# Lists

## What is a list?

Using the "split" string method from the preceding lesson, complete the get_word function to return the {n}th word from a passed sentence. For example, get_word("This is a lesson about lists", 4) should return "lesson", which is the 4th word in this sentence. Hint: remember that list indexes start at 0, not 1. 

```
def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("Nothing")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing
```

Output:

```
lesson
Nothing
Now
Nothing
```

## Modifying the Contents of a List

The skip_elements function returns a list containing every other element from an input list, starting with the first element. Complete this function to do that, using the for loop to iterate through the input list.

```
def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for ele in elements:
		# Does this element belong in the resulting list?
		if not i % 2:
			# Add this element to the resulting list
			new_list.append(ele)
		# Increment i
		i += 1

	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []
```

Output:

```
['a', 'c', 'e', 'g']
['Orange', 'Strawberry', 'Peach']
[]
```

## Lists and Tuples

Let's use tuples to store information about a file: its name, its type and its size in bytes. Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places. 

```
def file_size(file_info):
	name, type, size= file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21
```

Output:

```
17.46
0.48
1.21
```

## Iterating over Lists and Tuples

Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return every other element from the list, this time using the enumerate function to check if an element is on an even position or an odd position.

```
def skip_elements(elements):
	new_list = []
	for idx, ele in enumerate(elements):
		if not idx % 2:
			new_list.append(ele)
	
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
```

Output:

```
['a', 'c', 'e', 'g']
['Orange', 'Strawberry', 'Peach']
```

## List Comprehensions

The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the function, using list comprehension. Hint: remember that list and range counters start at 0 and end at the limit minus 1.

```
def odd_numbers(n):
	return [x for x in range(1, n+1) if x % 2]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []
```

Output:

```
[1, 3, 5]
[1, 3, 5, 7, 9]
[1, 3, 5, 7, 9, 11]
[1]
[]
```