## Practice Quiz: Interacting with the Command Line
* **Total points: 5**
* **Score: 100%**

<br>

### Question 1

Which of the following commands will redirect errors in a script to a file?

* user@ubuntu:~$ ./calculator.py >> error_file.txt
* **user@ubuntu:~$ ./calculator.py 2> error_file.txt**
* user@ubuntu:~$ ./calculator.py > error_file.txt
* user@ubuntu:~$ ./calculator.py < error_file.txt

> The "2>" sign will redirect errors to a file.

<br>

### Question 2

When running a kill command in a terminal, what type of signal is being sent to the process?

* PID
* SIGINT
* SIGSTOP
* **SIGTERM**

> The kill command sends a SIGTERM signal to a processor ID (PID) to terminate.

<br>

### Question 3

What is required in order to read from standard input using Python?

* echo file.txt
* cat file.txt
* The file descriptor of the STDIN stream
* **Stdin file object from sys module**

> Using sys.stdin, we can read from standard input in Python.

<br>

### Question 4

_____ are tokens delivered to running processes to indicate a desired action.

* **Signals**
* Methods
* Functions
* Commands

> Using signals, we can tell a program that we want it to pause or terminate, or many other possible commands.

<br>

### Question 5

In Linux, what command is used to display the contents of a directory?

* rmdir
* cp
* pwd
* **ls**

> The ls command lists the file contents of a directory.