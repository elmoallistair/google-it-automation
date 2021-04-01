## Interacting with the Command Line Shell

<br>

### Video: Basic Linux Commands

Which of the following Linux commands will create an empty file?

* **touch**
* pwd
* mkdir
* cd

> The touch command will create an empty file.

### Video: Redirecting Streams

How do you append the output of a command to a .txt file?

* user@ubuntu:~$ ./calculator.py > result.txt
* user@ubuntu:~$ ./calculator.py >> result.txt
* user@ubuntu:~$ ./calculator.py < result.txt
* user@ubuntu:~$ print("This will append")

> A double greater than sign will append a command output to a file.

<br>

### Video: Pipes and Pipelines

Which of the following is the correct way of using pipes?

* user@ubuntu:~$ cat sample.txt ./process.py
* user@ubuntu:~$ cat sample.txt || ./process.py
* user@ubuntu:~$ tr ' ' '\n' | sort | cat sample.txt
* **user@ubuntu:~$ cat sample.txt | tr ' ' '\n' | sort**

> The contents of the txt file are passed on to be placed in their own line and sorted in alphabetical order on the display.

<br>

### Video: Signalling Processes

What can you type in the terminal to stop the traceroute command from running cleanly?

* **Ctrl-C**
* SIGINT
* Ctrl-Z
* SIGSTOP

> This sends a SIGINT signal to the program to stop processing cleanly.

<br><hr><br>

## Bash Scripting

<br>

### Video: Creating Bash Scripts

Which command will correctly run a bash script?

* user@ubuntu:~$ #!/bin/bash
* user@ubuntu:~$ ./bash.py
* **user@ubuntu:~$ ./bash_sample.sh**
* user@ubuntu:~$ ./sh.bash

> A bash script is run with the .sh file extension.

<br>

### Video: Using Variables and Globs

When defining a variable you receive the "command not found" message. Which of the following commands will resolve this error?

* User1= billy
* $User2 =billy
* User3 = $billy
* **User4=billy**

> The variable "User4" has a value of "billy".

<br>

### Video: Conditional Execution in Bash

A conditional block in Bash that starts with 'if', ends with which of the following lines?

* **fi**
* if
* else
* grep

> The if conditional ends with fi (a backwards "if").

<br><hr><br>

## Advanced Bash Concept

<br>

### Video: For Loops in Bash Scripts

Which “for” conditional line will add users Paul and Jeremy to a user variable?

* for users in Paul Jeremy
* **for user in Paul Jeremy**
* for Paul Jeremy in user
* for Paul & Jeremy in user

> The elements Paul and Jeremy are added to the user variable.

<br>

### Video: Advanced Command Interaction

When using the following command, what would each line of the output start with?

`user@ubuntu:~$ tail /var/log/syslog | cut -d' ' -f3-`

* CRON[257236]:
* October
* 31
* **10:18:41**

> The time of the log will be shown with the -f3- or field three option of the cut command.

<br>

### Video: Choosing Between Bash and Python

Which of the following statements would make it better to start using Python instead of Bash?

* Operate with system commands.
* **Use on multi-platforms**.
* Operate with system files.
* Run a single process on multiple files.

> It is better to use Python and its standard library to use when working across multiple platforms.