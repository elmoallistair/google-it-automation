## Module 1 Graded Assessment
* **Total points: 10**
* **Score: 100%**

<br>

### Question 1

What is a computer program?
* A file that gets printed by the Python interpreter.
* The syntax and semantics of Python.
* The overview of what the computer will have to do to solve some automation problem.
* **A step-by-step recipe of what needs to be done to complete a task, that gets executed by the computer.**

> Being able to write such programs is a super useful skill that you'll acquire through this course.

<br>

### Question 2

What’s automation?
* The inputs and outputs of a program.
* **The process of replacing a manual step with one that happens automatically.**
* The checkout processes at a grocery store.
* The process of getting a haircut.

> By replacing a manual step with an automatic one we create automation that helps us reduce unnecessary manual work.

<br>

### Question 3

Which of the following tasks are good candidates for automation? Check all that apply.
* Writing a computer program.
* **Creating a report of how much each sales person has sold in the last month.**
* **Setting the home directory and access permissions for new employees joining your company.**
* Designing the new webpage for your company.
* Taking pictures of friends and family at a wedding.
* **Populating your company's e-commerce site with the latest products in the catalog.**

> Creating reports based on data are a great example of things that can be automated.

> The process of setting up the account for a new employee is usually repetitive and most of it can be automated.

> Automatically populating a website based on data is a great example of a task that can be automated.

<br>

### Question 4

* **What are some characteristics of the Python programming language? Check all that apply.**
* **Python programs are easy to write and understand.**
* The Python interpreter reads our code and transforms it into computer instructions.
* It's an outdated language that's barely in use anymore.
* **We can practice Python using web interpreters or codepads as well as executing it locally.**

> Because the syntax used by Python is similar to the one used by the English language, Python programs are easy to write and understand.

> We write our code using Python's syntax and semantics, and the interpreter transforms that into instructions that our computer executes.

> We can practice writing Python code with many different tools available to us, both online and offline.

<br>

### Question 5

How does Python compare to other programming languages?
* Python is the only programming language that is worth learning.
* **Each programming language has its advantages and disadvantages.**
* It's always better to use an OS specific language like Bash or Powershell than using a generic language like Python.
* Programming languages are so different that learning a second one is harder than learning the first one.

> Each language has its pros and cons. The best language to choose will depend on the problem you are trying to solve.

<br>

### Question 6

Write a Python script that outputs "Automating with Python is fun!" to the screen.

```
print("Automating with Python is fun!")
```

Output:

```
Automating with Python is fun!
```

<br>

### Question 7

Fill in the blanks so that the code prints "Yellow is the color of sunshine".

```
color = "Yellow"
thing = "sunshine"
print(color + " is the color of " + thing)
```

Output:

```
Yellow is the color of sunshine
```

<br>

### Question 8

Keeping in mind there are 86400 seconds per day, write a program that calculates how many seconds there are in a week, if a week is 7 days. Print the result on the screen.

Note: Your result should be in the format of just a number, not a sentence.

```
print(7 * 86400)
```

Output:

```
604800
```

<br>

### Question 9

Use Python to calculate how many different passwords can be formed with 6 lower case English letters. For a 1 letter password, there would be 26 possibilities. For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities. Using this information, print the amount of possible passwords that can be formed with 6 letters.

```
print(26 ** 6)
```

Output:

```
308915776
```

<br>

### Question 10

Most hard drives are divided into sectors of 512 bytes each. Our disk has a size of 16 GB. Fill in the blank to calculate how many sectors the disk has.

Note: Your result should be in the format of just a number, not a sentence.

```
disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size / sector_size

print(sector_amount)
```

Output:

```
33554432.0
```