## Strings

<br>

### Video: What is a string?

Modify the double_word function so that it returns the same word repeated twice, followed by the length of the new doubled word. For example, double_word("hello") should return hellohello10.

```
def double_word(word):
    return word*2 + str(len(word)*2)

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0
```

Output:

```
hellohello10
abcabc6
0
```

<br>

### Video: The Parts of a String

Want to give it a go yourself? Be my guest! Modify the first_and_last function so that it returns True if the first letter of the string is the same as the last letter of the string, False if they’re different. Remember that you can access characters using message[0] or message[-1]. Be careful how you handle the empty string, which should return True since nothing is equal to nothing.

```
def first_and_last(message):
    return message[0] == message[-1] if message else True

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
```

Output:

```
True
False
True
```

<br>

### Video: Creating New Strings

Using the index method, find out the position of "x" in "supercalifragilisticexpialidocious". 

```
word = "supercalifragilisticexpialidocious"
print(word.index('x'))
```

Output:

```
21
```

<br>

### Video: More String Methods

Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, in upper case. For example: "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”. 

```
def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS
```

Output:

```
USB
LAN
OS
```

<br>

### Video: Formatting Strings

Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam". For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".

```
def student_grade(name, grade):
	return f"{name} received {grade}% on the exam"

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))
```

Output:

```
Reed received 80% on the exam
Paige received 92% on the exam
Jesse received 85% on the exam
```

<br><hr><br>

## Lists

<br>

### Video: What is a list?

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

<br>

### Video: Modifying the Contents of a List

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

<br>

### Video: Lists and Tuples

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

<br>

### Video: Iterating over Lists and Tuples

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

<br>

### Video: List Comprehensions

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

<br><hr><br>

## Dictionaries

<br>

### Video: What is a dictionary?

The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 1) Add an entry for Epilogue on page 39. 2) Change the page number for Chapter 3 to 24. 3) Display the new dictionary contents. 4) Display True if there is Chapter 5, False if there isn't.

```
toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc['Epilogue'] = 39 # Epilogue starts on page 39
toc['Chapter 3'] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print('Chapter 5' in toc) # Is there a Chapter 5?
```

Output:

```
{'Introduction': 1, 'Chapter 1': 4, 'Chapter 2': 11, 'Chapter 3': 24, 'Chapter 4': 30, 'Epilogue': 39}
False
```

<br>

### Video: Iterating over the Contents of a Dictionary

Complete the code to iterate through the keys and values of the cool_beasts dictionary. Remember that the items method returns a tuple of key, value for each element in the dictionary. 

```
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for key, value in cool_beasts.items():
    print("{} have {}".format(key, value))
```

Output:

```
octopuses have tentacles
dolphins have fins
rhinos have horns
```

<br>

### Video: Dictionaries vs. Lists

In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be a list containing multiple values. Here we have a dictionary called "wardrobe" with items of clothing and their colors. Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.

```
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothing, colors in wardrobe.items():
	for color in colors:
		print("{} {}".format(color, clothing))
```

Output:

```
red shirt
blue shirt
white shirt
blue jeans
black jeans
```