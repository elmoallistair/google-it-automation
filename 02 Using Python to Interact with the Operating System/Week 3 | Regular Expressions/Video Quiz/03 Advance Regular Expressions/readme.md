# Advance Regular Expressions

## Capturing Groups

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

```
Here is your output:
John F. Kennedy
```

## More on Repetition Qualifiers

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

```
Here is your output:
['morning']\
['chocolate', 'afternoon']\
[]
```

## Extracting a PID Using regexes in Python

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

```
Here is your output:
12345 (ERROR)
None
None
67890 (RUNNING)
```

## Splitting and Replacing

We want to split a piece of text by either the word "a" or "the", as implemented in the following code. What is the resulting split list?

```
re.split(r"the|a", "One sentence. Another one? And the last one!")
```

* ['One sentence. Another one? And ', ' last one!']
* ['One sentence. Another one? And ', 'the', ' last one!']
* **['One sentence. Ano', 'r one? And ', ' l', 'st one!']**
* ['One sentence. Ano', 'the', 'r one? And ', 'the', ' l', 'a', 'st one!']