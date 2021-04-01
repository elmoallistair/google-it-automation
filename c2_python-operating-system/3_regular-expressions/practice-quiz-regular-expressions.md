## Practice Quiz: Regular Expressions
* **Total points: 5**
* **Score: 100%**

<br>

### Question 1

When using regular expressions, which of the following expressions uses a reserved character that can represent any single character?

* **re.findall(f.n, text)**
* re.findall(f*n, text)
* re.findall(fu$, text)
* re.findall(^un, text)

> The dot (.) represents any single character.

<br>

### Question 2

Which of the following is NOT a function of the Python regex module?

* re.search()
* re.match()
* re.findall()
* **re.grep()**

> The grep command utilizes regular expressions on Linux, but is not a part of the standard re Python module.

<br>

### Question 3

The circumflex [^] and the dollar sign [$] are anchor characters. What do these anchor characters do in regex?

* Match the start and end of a word.
* **Match the start and end of a line**
* Exclude everything between two anchor characters
* Represent any number and any letter character, respectively

> The circumflex and the dollar sign specifically match the start and end of a line.

<br>

### Question 4

When using regex, some characters represent particular types of characters. Some examples are the dollar sign, the circumflex, and the dot wildcard. What are these characters collectively known as?

* **Special characters**
* Anchor characters
* Literal characters
* Wildcard characters

> Special characters, sometimes called meta characters, give special meaning to the regular expression search syntax.

<br>

### Question 5

What is grep?

* An operating system
* A command for parsing strings in Python
* **A command-line regex tool**
* A type of special character

> The grep command is used to scan files for a string of characters occurring that fits a specified sequence.