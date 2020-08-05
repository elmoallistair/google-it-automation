# Code that Crashes

## Video: Accessing Invalid Memory

Which of the following can assist in finding out if invalid operations are occurring in a program running on a Windows system?

* Valgrind
* **Dr. Memory**
* PBD files
* Segfaults 

> Dr. Memory can assist in finding out if invalid operations are occurring in a program running on Windows or Linux.

<br>

## Video: Unhandled Errors and Exceptions

What can you use to notify users when an error occurs, the reason why it occurred, and how to resolve it?

* The pdb module
* **The logging module**
* Use printf debugging
* The echo command

> The logging module sets debug messages to show up when the code fails.

<br>

## Video: Fixing Someone Else's Code

After getting acquainted with the program’s code, where might you start to fix a problem?

* Run through tests
* Read the comments
* **Locate the affected function**
* Create new tests 

> Start working on the function that produced the error, and the function(s) that called it. 

<br>

## Video: Debugging a Segmentation Fault

When debugging code, what command can you use to figure out how your program reached the failed state?

* gdb
* **backtrace**
* ulimit
* list 

> The backtrace command can be used to show a summary of the function calls that were used to the point where the failure occurs. 

<br>

## Video: Debugging a Python Crash

When debugging in Python, what command can you use to run the program until it crashes with an error?

* pdb3
* next
* **continue**
* KeyError

> Running the continue command after starting the pdb3 debugger will execute the program until it finishes or crashes.