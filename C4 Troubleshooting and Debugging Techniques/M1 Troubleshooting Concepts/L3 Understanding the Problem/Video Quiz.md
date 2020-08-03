# Understanding the Problem

<br>

## Video: "It Doesn't Work"

When a user reports that a "website doesn't work," what is an appropriate follow-up question you can use to gather more information about the problem?

* **What steps did you perform?**
* Is the server receiving power?
* What server is the website hosted on?
* Do you have support ticket number? 

> Asking the user what steps they performed will help you gather more information in order to better understand and isolate the problem.

<br>

## Video: Creating a Reproduction Case

A program fails with an error, “No such file or directory.” You create a directory at the expected file path and the program successfully runs. Describe the reproduction case you’ll submit to the program developer to verify and fix this error.

* **A report explaining to open the program without the specific directory on the computer**
* A report with application logs exported from Windows Event Viewer 
* A report listing the contents of the new directory
* A report listing the differences between strace and ltrace logs. 

> This a specific way to reproduce the error and verify it exists. The developer can work on fixing it right away. 

<br>

## Video: Finding the Root Cause

Generally, understanding the root cause is essential for _____?

* Purchasing new devices
* Producing test data
* Avoiding interfering with users
* **Providing the long-term resolution**

> Understanding the root cause is essential for providing the long-term resolution. 

<br>

## Video: Dealing with Intermittent Issues

What sort of software bug might we be dealing with if power cycling resolves a problem?

* **Poorly managed resources**
* A heisenbug
* Logs filling up
* A file remains open 

> Power cycling releases resources stored in cache or memory, which gets rid of the problem. 