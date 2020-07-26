# Introduction to Python

<br>

## Video: What is Python?

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

## Video: Why is Python relevant to IT?

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

## Video: Other Languages

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