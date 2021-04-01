## Practice Quiz: Python Subprocesses
* **Total points: 5**
* **Score: 100%**

<br>

### Question 1

What type of object does a run function return?

* stdout
* **CompletedProcess**
* capture_output
* returncode

> This object includes information related to the execution of a command.

<br>

### Question 2

How can you change the current working directory where a command will be executed?

* Use the env parameter.
* Use the shell parameter.
* **Use the cwd parameter.**
* Use the capture_output parameter.

> This will `change the current working directory where the command will be executed.

<br>

### Question 3

When a child process is run using the subprocess module, which of the following are true? (check all that apply)

* **The child process is run in a secondary environment.**
* **The parent process is blocked while the child process finishes.**
* The parent process and child process both run simultaneously.
* **Control is returned to the parent process when the child process ends.**

> To run the external command, a secondary environment is created for the child subprocess, where the command is executed.

> While the parent process is waiting on the subprocess to finish, it’s blocked, meaning the parent can’t do any work until the child finishes.

> After the external command completes its work, the child process exits, and the flow of control returns to the parent.

<br>

### Question 4

When using the run command of the subprocess module, what parameter, when set to True, allows us to store the output of a system command?

* cwd
* **capture_output**
* timeout
* shell

> The capture_output parameter allows us to get and store the output of the system command we're using.

<br>

### Question 5

What does the copy method of os.environ do?

* **Creates a new dictionary of environment variables**
* Runs a second instance of an environment
* Joins two strings
* Removes a file from a directory

> The copy method of os.environ makes a new copy of the dictionary containing the environment variables, making modification easier.