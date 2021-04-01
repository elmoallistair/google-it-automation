## Understanding Slowness

<br>

### Video: Why is my computer slow?

When addressing slowness, what do you need to identify?

* **The bottleneck**
* The device
* The script
* The system 

> The bottleneck could be the CPU time, or time spent reading data from disk.

<br>

### Video: How Computers Use Resources

After retrieving data from the network, how can an application access that same data quicker next time?

* Use the swap
* **Create a cache**
* Use memory leak
* Store in RAM

> A cache stores data in a form that's faster to access than its original form.

<br>

### Video: Possible Causes of Slowness

A computer becomes sluggish after a few days, and the problem goes away after a reboot. Which of the following is the possible cause?

* Files are growing too large.
* **A program is keeping some state while running.**
* Files are being read from the network.
* Hard drive failure.

> A program keeping a state without any change can slow down a computer up until it is rebooted.

<br><hr><br>

## Slow Code

<br>

### Video: Writting Efficient Code

What is the cProfile module used for?

* For parsing files.
* To analyze a C program.
* **To count functions calls**
* To remove unnecessary functions.

> The cProfile module is used to count how many times functions are called, and how long they run.

<br>

### Video: Using the Right Data Structures

Which of the following has values associated with keys in Python?

* A hash
* **A dictionary**
* A HashMap
* An Unordered Map

> Python uses a dictionary to store values, each with a specific key

<br>

### Video: Expensive Loops

Your Python script searches a directory, and runs other tasks in a single loop function for 100s of computers on the network. Which action will make the script the least expensive?

* **Read the directory once**
* Loop the total number of computers
* Service only half of the computers
* Use more memory 

> Reading the directory once before the loop will make the script less expensive to run.

<br>

### Video: Keeping Local Results

Your script calculates the average number of active user sessions during business hours in a seven-day period. How often should a local cache be created to give a good enough average without updating too often?

* Once a week
* **Once a day**
* Once a month
* Once every 8 hours 

> A local cache for every day can be accessed quickly, and processed for a seven-day average calculation. 

<br>

### Video: Slow Script with Expensive Loop

You use the time command to determine how long a script runs to complete its various tasks. Which output value will show the time spent doing operations in the user space?

* Real
* Wall-clock
* Sys
* **User**

> The user value is the time spent doing operations in the user space. 

<br><hr><br>

## Understanding Slowness

<br>

### Video: Why is my computer slow?

When addressing slowness, what do you need to identify?

* **The bottleneck**
* The device
* The script
* The system 

> The bottleneck could be the CPU time, or time spent reading data from disk.

<br>

### Video: How Computers Use Resources

After retrieving data from the network, how can an application access that same data quicker next time?

* Use the swap
* **Create a cache**
* Use memory leak
* Store in RAM

> A cache stores data in a form that's faster to access than its original form.

<br>

### Video: Possible Causes of Slowness

A computer becomes sluggish after a few days, and the problem goes away after a reboot. Which of the following is the possible cause?

* Files are growing too large.
* **A program is keeping some state while running.**
* Files are being read from the network.
* Hard drive failure.

> A program keeping a state without any change can slow down a computer up until it is rebooted.

<br><hr><br>

## When Slowness Problems Get Complex

<br>

### Video: Parallelizing Operations

A script is _____ if you are running operations in parallel using all available CPU time.

* I/O bound
* Threading
* **CPU bound**
* Asyncio 

>  A script is CPU bound if you're running operations in parallel using all available CPU time.

<br>

### Video: Slowly Growing in Complexity

You’re creating a simple script that runs a query on a list of product names of a very small business, and initiates automated tasks based on those queries. Which of the following would you use to store product names?

* SQLite
* Microsoft SQL Server
* Memcached
* **CSV file**

> A simple CSV file is enough to store a list of product names. 

<br>

### Video: Dealing with Complex Slow Systems

A company has a single web server hosting a website that also interacts with an external database server. The web server is processing requests very slowly. Checking the web server, you found the disk I/O has high latency. Where is the cause of the slow website requests most likely originating from?

* **Local disk**
* Remote database
* Slow Internet
* Database index 

> The local disk I/O latency is causing the application to wait too long for data from disk. 

<br>

### Video: Using Threads to Make Things Go Faster

Which module makes it possible to run operations in a script in parallel that makes better use of CPU processing time?

* Executor
* **Futures**
* Varnish
* Concurrency 

> The futures module makes it possible to run operations in parallel using different executors. 

<br><hr><br>

## When Slowness Problems Get Complex

<br>

### Video: Parallelizing Operations

A script is _____ if you are running operations in parallel using all available CPU time.

* I/O bound
* Threading
* **CPU bound**
* Asyncio 

>  A script is CPU bound if you're running operations in parallel using all available CPU time.

<br>

### Video: Slowly Growing in Complexity

You’re creating a simple script that runs a query on a list of product names of a very small business, and initiates automated tasks based on those queries. Which of the following would you use to store product names?

* SQLite
* Microsoft SQL Server
* Memcached
* **CSV file**

> A simple CSV file is enough to store a list of product names. 

<br>

### Video: Dealing with Complex Slow Systems

A company has a single web server hosting a website that also interacts with an external database server. The web server is processing requests very slowly. Checking the web server, you found the disk I/O has high latency. Where is the cause of the slow website requests most likely originating from?

* **Local disk**
* Remote database
* Slow Internet
* Database index 

> The local disk I/O latency is causing the application to wait too long for data from disk. 

<br>

### Video: Using Threads to Make Things Go Faster

Which module makes it possible to run operations in a script in parallel that makes better use of CPU processing time?

* Executor
* **Futures**
* Varnish
* Concurrency 

> The futures module makes it possible to run operations in parallel using different executors. 