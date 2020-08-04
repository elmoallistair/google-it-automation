# When Slowness Problems Get Complex

<br>

## Video: Parallelizing Operations

A script is _____ if you are running operations in parallel using all available CPU time.

* I/O bound
* Threading
* **CPU bound**
* Asyncio 

>  A script is CPU bound if you're running operations in parallel using all available CPU time.

<br>

## Video: Slowly Growing in Complexity

You’re creating a simple script that runs a query on a list of product names of a very small business, and initiates automated tasks based on those queries. Which of the following would you use to store product names?

* SQLite
* Microsoft SQL Server
* Memcached
* **CSV file**

> A simple CSV file is enough to store a list of product names. 

<br>

## Video: Dealing with Complex Slow Systems

A company has a single web server hosting a website that also interacts with an external database server. The web server is processing requests very slowly. Checking the web server, you found the disk I/O has high latency. Where is the cause of the slow website requests most likely originating from?

* **Local disk**
* Remote database
* Slow Internet
* Database index 

> The local disk I/O latency is causing the application to wait too long for data from disk. 

<br>

## Video: Using Threads to Make Things Go Faster

Which module makes it possible to run operations in a script in parallel that makes better use of CPU processing time?

* Executor
* **Futures**
* Varnish
* Concurrency 

> The futures module makes it possible to run operations in parallel using different executors. 