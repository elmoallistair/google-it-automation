## String Reference Cheat Sheet

<hr>

In Python, there are a lot of things you can do with strings. In this cheat sheet, you’ll find the most common string operations and string methods.

**String operations**

* `len(string)` Returns the length of the string
* for character in string Iterates over each character in the string
* if substring in string Checks whether the substring is part of the string
* `string[i]` Accesses the character at index i of the string, starting at zero
* `string[i:j]` Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.

**String methods**

* `string.lower()` / `string.upper()` Returns a copy of the string with all lower / upper case characters
* `string.lstrip()` / `string.rstrip()` / `string.strip()` Returns a copy of the string without left / right / left or right whitespace
* `string.count(substring)` Returns the number of times substring is present in the string
* `string.isnumeric()` Returns True if there are only numeric characters in the string. If not, returns False.
* `string.isalpha()` Returns True if there are only alphabetic characters in the string. If not, returns False.
* `string.split()` / `string.split(delimiter)` Returns a list of substrings that were separated by whitespace / delimiter
* `string.replace(old, new)` Returns a new string where all occurrences of old have been replaced by new.
* `delimiter.join(list of strings)` Returns a new string with all the strings joined by the delimiter 

Check out the official documentation for [all available String methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

