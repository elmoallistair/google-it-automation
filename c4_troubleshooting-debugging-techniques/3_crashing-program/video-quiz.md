## Why Programs Crash

<br>

### Video: System That Crash

A user reported an application crashes on their computer. You log in and try to run the program and it crashes again. Which of the following steps would you perform next to reduce the scope of the problem?

* Check the health of the RAM
* Switch the hard drive into another computer
* Check the health of the hard drive
* **Review application logs**

> Reviewing logs is the next best step to determine if logs reveal any reason for the crash. 

<br>

### Video: Understanding Crashing Applications

Where should you look for application logs on a Windows system?

* The /var/log directory
* The .xsession-errors file
* The Console app
* **The Event Viewer app**

> The Event Viewer app contains logs on a Windows system. 

<br>

What to do when you can't fix the program?

An application fails in random intervals after it was installed on a different operating system version. What can you do to work around the issue?

* Use a wrapper
* **Use a container**
* Use a watchdog
* Use an XML format 

> A container allows the application to run in its own environment without interfering with the rest of the system. 

<br>

### Video: Internal Server Error

Where is a common location to view configuration files for a web application running on a Linux server?

* **/etc/<app folder>**
* /var/log/<app folder>
* /srv/<app folder>
* /<app folder> 

> The /etc directory will contain the application folder that stores configuration files. 

<br><hr><br>

## Code that Crashes

### Video: Accessing Invalid Memory

Which of the following can assist in finding out if invalid operations are occurring in a program running on a Windows system?

* Valgrind
* **Dr. Memory**
* PBD files
* Segfaults 

> Dr. Memory can assist in finding out if invalid operations are occurring in a program running on Windows or Linux.

<br>

### Video: Unhandled Errors and Exceptions

What can you use to notify users when an error occurs, the reason why it occurred, and how to resolve it?

* The pdb module
* **The logging module**
* Use printf debugging
* The echo command

> The logging module sets debug messages to show up when the code fails.

<br>

### Video: Fixing Someone Else's Code

After getting acquainted with the program’s code, where might you start to fix a problem?

* Run through tests
* Read the comments
* **Locate the affected function**
* Create new tests 

> Start working on the function that produced the error, and the function(s) that called it. 

<br>

### Video: Debugging a Segmentation Fault

When debugging code, what command can you use to figure out how your program reached the failed state?

* gdb
* **backtrace**
* ulimit
* list 

> The backtrace command can be used to show a summary of the function calls that were used to the point where the failure occurs. 

<br>

### Video: Debugging a Python Crash

When debugging in Python, what command can you use to run the program until it crashes with an error?

* pdb3
* next
* **continue**
* KeyError

> Running the continue command after starting the pdb3 debugger will execute the program until it finishes or crashes.

<br><hr><br>

## Handling Bigger Incidents

<br>

### Video: Crashes in Complex Systems

A website is producing service errors when loading certain pages. Looking at the logs, one of three web servers isn’t responding correctly to requests. What can you do to restore services, while troubleshooting further?

* Deploy a new web server
* Roll back application changes
* **Remove the server from the pool**
* Create standby servers 

> Removing the server from the pool will provide full service to users from the remaining web servers 

<br>

### Video: Communication and Documenting During Incidents

Which of the following persons is responsible for communicating with customers that are affected by an access issue with a website?

* **Communications lead**
* Manager
* Incident controller
* Software engineer 

> The communications lead provides timely updates on the incident and answers questions from users. 

<br>

### Video: Writing Effective Postmortems

When writing an effective postmortem of an incident, what should you NOT include?

* What caused the issue
* **Who caused the issue**
* What the impact was
* The short-term remediation 

> A postmortem of an incident should not include the person(s) who caused the issue. 