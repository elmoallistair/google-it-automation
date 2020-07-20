## Regular Expressions

<hr>

### Video: What are regular expressions?

Which of the following demonstrates how regex (regular expressions) might be used?

* Recognize an image
* Calculate Pi
* **Find strings of text that match a pattern**
* Multiply and divide arrays

### Video: Why use regular expressions?

Rather than using the index() function of the string module, we can use regular expressions, which are more flexible. After importing the regular expression module re, what regex function might be used instead of standard methods?

* re.regex()
* re.pid()
* **re.search()**
* re.index()

### Video: Basic Matching with grep

Using the terminal, which of the following commands will correctly use grep to find the words “sling” and “sting” (assuming they are in our file, file.txt)?

* user@ubuntu:~$ grep(s.ing) /usr/file.txt
* user@ubuntu:~$ grep sting+sling /usr/file.txt
* **user@ubuntu:~$ grep s.ing /usr/file.txt**
* user@ubuntu:~$ grep s+ing /usr/file.txt

## Basic Regular Expressions

<hr>

### Video: Simple Matching in Python

Fill in the code to check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between.

```
import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True
```

### Video: Wildcards and Character Classes

Fill in the code to check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.

```
import re
def check_punctuation (text):
  result = re.search(r"[,.:;?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False
```

### Video: Repetition Qualifiers

The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False. Fill in the code to make this work. 

```
import re
def repeating_letter_a(text):
  result = re.search(r"[Aa].*[Aa]", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True
```

### Video: Escaping Characters

Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.

```
import re
def check_character_groups(text):
  result = re.search(r"[0-9]\w", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False
```