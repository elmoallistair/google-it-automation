## Regular Expressions

<br>

### Video: What are regular expressions?

Which of the following demonstrates how regex (regular expressions) might be used?

* Recognize an image
* Calculate Pi
* **Find strings of text that match a pattern**
* Multiply and divide arrays

<br>

### Video: Why use regular expressions?

Rather than using the index() function of the string module, we can use regular expressions, which are more flexible. After importing the regular expression module re, what regex function might be used instead of standard methods?

* re.regex()
* re.pid()
* **re.search()**
* re.index()

<br>

### Video: Basic Matching with grep

Using the terminal, which of the following commands will correctly use grep to find the words “sling” and “sting” (assuming they are in our file, file.txt)?

* user@ubuntu:~$ grep(s.ing) /usr/file.txt
* user@ubuntu:~$ grep sting+sling /usr/file.txt
* **user@ubuntu:~$ grep s.ing /usr/file.txt**
* user@ubuntu:~$ grep s+ing /usr/file.txt

<br><hr><br>

## Basic Regular Expressions

<br>

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

Output:

```
True
False
True
```

<br>

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

Output:

```
True
False
True
True
False
```

<br>

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

Output:

```
True
False
True
True
```

<br>

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

Output:

```
False
True
True
False
```

<br>

### Video: Regular Expressions in Action

Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point. 

```
import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z| ]*[.?!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
```

Output:

```
True
False
False
False
True
```

<br><hr><br>

## Advance Regular Expressions

<br>

### Video: Capturing Groups

Fix the regular expression used in the rearrange_name function so that it can match middle names, middle initials, as well as double surnames.

```
import re
def rearrange_name(name):
  result = re.search(r'^([\w \.-]*), ([\w \.-]*)', name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)
```

Output:

```
John F. Kennedy
```

<br>

### Video: More on Repetition Qualifiers

The long_words function returns all words that are at least 7 characters. Fill in the regular expression to complete this function.

```
import re
def long_words(text):
  pattern = r'\w{7,}'
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []
```

Output:

```
['morning']
['chocolate', 'afternoon']
[]
```

<br>

### Video: Extracting a PID Using regexes in Python

Add to the regular expression used in the extract_pid function, to return the uppercase message in parenthesis, after the process id.

```
import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]: (\w+)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1],result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)
```

Output:

```
12345 (ERROR)
None
None
67890 (RUNNING)
```

<br>

### Video: Splitting and Replacing

We want to split a piece of text by either the word "a" or "the", as implemented in the following code. What is the resulting split list?

```
re.split(r"the|a", "One sentence. Another one? And the last one!")
```

* `['One sentence. Another one? And ', ' last one!']`
* `['One sentence. Another one? And ', 'the', ' last one!']`
* **`['One sentence. Ano', 'r one? And ', ' l', 'st one!']`**
* `['One sentence. Ano', 'the', 'r one? And ', 'the', ' l', 'a', 'st one!']`