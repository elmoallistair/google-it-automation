## Practice Quiz: Processing Log Files
* **Total points: 5**
* **Score: 100%**

<br>

### Question 1

You have created a Python script to read a log of users running CRON jobs. The script needs to accept a command line argument for the path to the log file. Which line of code accomplishes this?

* import sys
* **syslog=sys.argv[1]**
* print(line.strip())
* usernames = {}

> This will assign the script's first command line argument to the variable "syslog".

<br>

### Question 2

Which of the following is a data structure that can be used to count how many times a specific error appears in a log?

* **Dictionary**
* Get
* Continue
* Search

> A dictionary is useful to count appearances of strings.

<br>

### Question 3

Which keyword will return control back to the top of a loop when iterating through logs?

* **Continue**
* Get
* With
* Search

> The continue statement is used to return control back to the top of a loop.

<br>

### Question 4

When searching log files using regex, which regex statement will search for the alphanumeric word "IP" followed by one or more digits wrapped in parentheses using a capturing group?

* `r"IP \(\d+\)$"`
* `b"IP \((\w+)\)$"`
* **`r"IP \((\d+)\)$"`**
* `r"IP \((\D+)\)$"`

> This expression will search for the word "IP" followed by a space and parentheses. It uses a capture group and \d+ to capture any digit characters found in the parentheses.

<br>

### Question 5

Which of the following are true about parsing log files? (Select all that apply.)

* Load the entire log files into memory.
* **You should parse log files line by line.**
* **It is efficient to ignore lines that don't contain the information we need.**
* **We have to open() the log files first.**

> Since log files can get pretty large, it's a good idea to parse them one line at a time instead of loading the entire file into memory at once.

> We can save a lot of time by not parsing lines that don't contain what we need.

> Before we can parse our log file, we have to use the open() or with open() command on the file first.