# Interacting with the Command Line Shell

<br>

## Video: Basic Linux Commands

Which of the following Linux commands will create an empty file?

* **touch**
* pwd
* mkdir
* cd

> The touch command will create an empty file.

## Video: Redirecting Streams

How do you append the output of a command to a .txt file?

* user@ubuntu:~$ ./calculator.py > result.txt
* user@ubuntu:~$ ./calculator.py >> result.txt
* user@ubuntu:~$ ./calculator.py < result.txt
* user@ubuntu:~$ print("This will append")

> A double greater than sign will append a command output to a file.

<br>

## Video: Pipes and Pipelines

Which of the following is the correct way of using pipes?

* user@ubuntu:~$ cat sample.txt ./process.py
* user@ubuntu:~$ cat sample.txt || ./process.py
* user@ubuntu:~$ tr ' ' '\n' | sort | cat sample.txt
* **user@ubuntu:~$ cat sample.txt | tr ' ' '\n' | sort**

> The contents of the txt file are passed on to be placed in their own line and sorted in alphabetical order on the display.

<br>

## Video: Signalling Processes

What can you type in the terminal to stop the traceroute command from running cleanly?

* **Ctrl-C**
* SIGINT
* Ctrl-Z
* SIGSTOP

> This sends a SIGINT signal to the program to stop processing cleanly.