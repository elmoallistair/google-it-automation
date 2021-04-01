## Introduction to Programming

<br>

### Video: What is programming?

Why do we need to learn the syntax and semantics of a programming language?

* To be able to easily switch to a different programming language
* So that we know which part is the subject and which one is the predicate
* **To allow us to clearly express what we want the computer to do**
* To understand why our computer crashes

> Knowing the syntax and understanding the semantics of a programming language allows us to tell the computer what we want it to do.

<br>

### Video: What is automation?

What’s automation?

* The process of telling a computer what to do
* The process of installing traffic lights
* The process of getting a haircut
* **The process of replacing a manual step with one that happens automatically**

> By replacing a manual step with an automatic one we create automation that helps us reduce unnecessary manual work.

<br>

### Video: Getting Computers to Work for You

Which of the following tasks do you think are good candidates for automation? Check all that apply.

* **Periodically scanning the disk usage of a group of fileservers**
* **Installing software on laptops given to new employees when they are hired**
* Investigating reports that customers are having difficulty accessing your company's external website
* Designing a configuration management system for deploying software patches

> Scanning the disk usage is a task that can be easily automated. By letting the computer do it, you won't have to worry about forgetting to do it whenever it's needed.

> Installing and configuring software is a task that can be automated. Ensuring that everyone gets the exact same setup and reducing the amount of manual work needed for each new employee.

<br><hr><br>

## Introduction to Python

<br>

### Video: What is Python?

Execute the following code and see what happens. Feel free to change it and run it as many times as you want.

```
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)
```

Output:

```
Hi Taylor
Hi Alex
Hi Pat
Hi Eli
```

<br>

### Video: Why is Python relevant to IT?

Select all options that explain why Python is relevant to today’s IT industry.

* **Python scripts are easy to write, understand, and maintain.**
* **There are many system administration tools built with Python.**
* Python was written by Guido van Rossum in 1991.
* **Python is available on a wide variety of platforms.**
* There have been multiple major version releases over the years which incorporate significant changes to the language.

> Python is a language that tries to mimic our natural language and so Python scripts are generally easy to write, understand and maintain.

> Over the years, the Python community has developed a lot of additional tools that can be used by system administrators to get their job done.

> Python is available on Windows, Linux, MacOS and even on mobile devices, making it a great tool for IT specialist looking to create scripts that can work across platforms.

<br>

### Video: Other Languages

Here's how printing "Hello, World" 10 times looks in Bash and Powershell:

**Bash:**

```
for i in {1..10}; do
  echo Hello, World!
done
```

**Powershell:**

```
for ($i=1; $i -le 10; $i++) { 
  Write-Host "Hello, World!"
}
```

Now try out the Python example yourself:

```
for i in range(10):
  print("Hello, World!")
```

Output:

```
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
Hello, World!
```

<br><hr><br>

## Hello World

<br>

### Video: Hello, World!

Write a Python script that outputs "I'm programming in Python!" to the screen. Remember that you need to use the print() function and use quotation marks to delimiter the string.

```
print("I'm programming in Python!")
```

Output:

```
I'm programming in Python!
```

<br>

### Video: Getting Information from the User

In the following script, change the values of color and thing to have the computer output a different statement than the initial one.

```
color = "Blue"
thing = "Sky"
print(color + " is the color of " + thing)
```

Output:

```
Blue is the color of Sky
```

<br>

### Video: Python Can Be Your Calculator

Use Python to calculate (((1+2)*3)/4)<sup>5</sup>

**Tip**: remember that you can use a**b to calculate a to the power of b. 

```
print((((1+2)*3)/4)**5)
```

Output:

```
57.6650390625
```