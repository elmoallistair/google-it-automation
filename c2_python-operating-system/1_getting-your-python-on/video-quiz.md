## Getting Ready for Python

<br>

### Video: Getting Familiar with the Operating System

Which of the following is NOT an open-source OS?

* Ubuntu Linux
* FreeBSD
* Android
* **Microsoft Windows**

> The Windows operating system is a proprietary OS developed exclusively by Microsoft.

<br>

### Video: Getting Your Computer Ready for Python

What is the name of the command line tool commonly used to install, update, and remove external Python modules mentioned in the video?

* **pip**
* PyPI
* python3 --version
* conda

> pip is a cross-platform tool called a package manager used to install, update, or remove external Python modules.

<br><hr><br>

## Running Python Locally

<br>

### Video: Interpreted vs. Compiled Languages

Which of the following programming languages are interpreted languages?

* Java and C#
* **Python and Javascript**
* C++ and Go
* C and Rust

> Interpreted languages trade off slightly slower runtime performance—removing the need for compiling—by using programs called interpreters to execute the code.

<br>

### Video: How to Run a Python Script

What is the purpose of using a shebang line in a Python file?

* To tell the operating system where to find programs to execute.
* To tell the operating system to execute a file in the current directory.
* **To specify beforehand what command to use when running the script.**
* To make the specified file executable by changing permissions.

> Inserting a shebang line (such as #!/usr/bin/env python3) as the first line tells the operating system what command we want to use to execute the script.

<br>

### Video: Your Own Python Modules

Proper code reuse is important, so let’s see if you were paying attention. Which of the following lines will allow you to use the datetime module in your script?

* use datetime
* using datetime
* date_time = datetime
* **import datetime**

> We use the import command to import any module located in the PATH directory. We can also use import as to assign a localName variable to the imported module.

<br>

### Video: What is an IDE?

Which of the following is NOT an example of code completion?

* After you type the letters “ret”, your IDE finishes your sentence with return.
* After typing the opening parentheses after a function, your IDE inputs the final parentheses.
* **After typing “def”, your IDE detects that you are typing a function and highlights it.**
* After typing the first few letters of an existing variable, your IDE suggests that variable, highlighting the suggestion.

> Syntax highlighting detects the language we’re writing our code in and highlights the pieces of code that make up the syntax of the language.

<br><hr><br>

## Automating Tasks Through Programming

<br>

### Benefits of Automation

In terms of automation, which of the following is an example of scalability?

* You fix an error in a script and it’s fixed there, once and forever.
* **An IT engineer writes a script to compile a report on each machine's uptime and downtime for the day and email it to relevant parties every evening.**
* A company hires more IT staff to keep up with work levels.
* Minimizing workloads to stay within current productivity levels

> Scalability means that when more work is added to a system, the system can do whatever it needs to complete the work.

<br>

### Pitfals of Automation

Which of the following correctly describes the Pareto Principle?

* If we estimate that it’d take less time to automate the task than to do it manually, chances are it’s a good candidate for automation.
* **One fifth of the sysadmin tasks you perform comprise four fifths of your total workload.**
* Is the time and effort it takes to write the script worth the potential automation benefits?
* Four fifths of the sysadmin tasks you perform comprise one fifth of your total workload.

> The Pareto Principle states that 20% of the system administration tasks you perform are responsible for 80% of your workload. Therefore, identifying and automating those tasks will put your productivity through the roof!

<br>

### Practical Automation Example

Which of the following could be a good example of when to use an automation script?

* Automate a process you might never use again
* Automate a five-minute process that occurs once every six months
* Automate a process that will take longer to implement than it takes to do manually
* **Detect dangerously high CPU usage levels across a network and scale back the CPU clock speeds of those devices, or shut them down to prevent overheating**

> These days most consumer devices do this on their own, but in the case of custom hardware or other specific use cases such as cluster networks, automation would fit this task nicely and reduce failover.