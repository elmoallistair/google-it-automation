# Basic Linux Commands Cheat-Sheet

This list includes a bunch of different commands that are useful to know when working with Linux. Not all of these commands are covered in the videos, so feel free to investigate them on your own.

### Managing files and directories

* **cd** directory: changes the current working directory to the specified one
* **pwd**: prints the current working directory
* **ls**: lists the contents of the current directory
* **ls** directory: lists the contents of the received directory
* **ls** -l: lists the additional information for the contents of the directory
* **ls** -a: lists all files, including those hidden
* **ls** -la: applies both the -l and the -a flags 
* **mkdir** directory: creates the directory with the received name
* **rmdir** directory: deletes the directory with the received name (if empty)
* **cp** old_name new_name: copies old_name into new_name
* **mv** old_name new_name: moves old_name into new_name
* **touch** file_name: creates an empty file or updates the modified time if it exists
* **chmod** modifiers files: changes the permissions for the files according to the provided modifiers; we've seen +x to make the file executable
* **chown** user files: changes the owner of the files to the given user
* **chgrp** group files: changes the group of the files to the given group

### Operating with the content of files

* **cat** file: shows the content of the file through standard output
* **wc** file: counts the amount of characters, words, and lines in the given file; can also count the same values of whatever it receives via stdin
* **file** file: prints the type of the given file, as recognized by the operating system
* **head** file: shows the first 10 lines of the given file
* **tail** file: shows the last 10 lines of the given file
* **less** file: scrolls through the contents of the given file (press "q" to quit)
* **sort** file: sorts the lines of the file alphabetically
* **cut** -dseparator -ffields file: for each line in the given file, splits the line according to the given separator and prints the given fields (starting from 1)

### Additional commands

* **echo** "message": prints the message to standard output
* **date**: prints the current date
* **who**: prints the list of users currently logged into the computer
* **man** command: shows the manual page of the given command; manual pages contain a lot of information explaining how to use each command (press "q" to quit)
* **uptime**: shows how long the computer has been running
* **free**: shows the amount of unused memory on the current system 

<br>

# Redirections, Pipes and Signals

### Managing streams

These are the redirectors that we can use to take control of the streams of our programs

* command **>** file: redirects standard output, overwrites file
* command **>>** file: redirects standard output, appends to file
* command **<** file: redirects standard input from file
* command **2>** file: redirects standard error to file
* command1 **|** command2: connects the output of command1 to the input of command2

### Operating with processes

These are some commands that are useful to know in Linux when interacting with processes. Not all of them are explained in videos, so feel free to investigate them on your own.

* **ps**: lists the processes executing in the current terminal for the current user
* **ps** ax: lists all processes currently executing for all users
* **ps** e: shows the environment for the processes listed 
* **kill** PID: sends the SIGTERM signal to the process identified by PID
* **fg**: causes a job that was stopped or in the background to return to the foreground
* **bg**: causes a job that was stopped to go to the background
* **jobs**: lists the jobs currently running or stopped
* **top**: shows the processes currently using the most CPU time (press "q" to quit) 