## Data Streams

<br>

### Video: Reading Data interactively

Which line of code from the `seconds.py` script will convert all integer inputs into seconds?

* int(input("Enter the number of seconds: "))
* int(input("Enter the number of minutes: "))
* int(input("Enter the number of hours: "))
* **to_seconds(hours, minutes, seconds)**

> This line of code uses a function to convert the number of hours, minutes, and seconds into seconds.

<br>

### Video: Standard Streams

Which I/O stream is the output function using when showing an error message?

* STDIN
* STDOUT
* **STDERR**
* PRINT

> STDERR displays output specifically for error messages.

<br>

### Video: Environment Variables

Which directory is NOT listed in the PATH variable by default?

* /usr/local/sbin
* **/usr/sbin/temp**
* /bin
* /sbin

> This directory is not listed by default. 

<br>

### Video: Command-Line Arguments and Exit Status

Where are the command line arguments stored?

* argv
* **sys**
* parameters&#46;py
* print

> The list of arguments are stored in the sys module.

<br><hr><br>

## Python Subprocesses

<br>

### Video: Running System Commands in Python

A system command that sends ICMP packets can be executed within a script by using which of the following?

* **subprocess.run**
* Ping
* CompletedProcess
* Arguments

> This function will execute a system command such as ping.

<br>

### Video: Obtaining the Output of a System Command

Which of the following is a Unicode standard used to convert an array of bytes into a string?

* **UTF-8**
* stdout
* capture_output
* Host

> This encoding is part of the Unicode standard that can transform an array of bytes into a string.

<br>

### Video: Advanced Subprocess Management

Which method do you use to prepare a new environment to modify environment variables?

* join
* env
* **copy**
* cwd

> Calling this method of the os.environ dictionary will copy the current environment variables to store and prepare a new environment.

<br><hr><br>

## Processing Log Files

<br>

### Video: Filtering Log Files with Regular Expressions

We're using the same syslog, and we want to display the date, time, and process id that's inside the square brackets. We can read each line of the syslog and pass the contents to the show_time_of_pid function. Fill in the gaps to extract the date, time, and process id from the passed line, and return this format: Jul 6 14:01:23 pid:29440.
```
import re
def show_time_of_pid(line):
  pattern = r"([a-zA-Z]+ \d+ \d+:\d+:\d+).*\[(\d+)\]\:"
  result = re.search(pattern, line)
  return "{} pid:{}".format(result.group(1), result.group(2))

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440
print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187
print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187
print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440
print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807
print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440
print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440
```
Output:

```
Jul 6 14:01:23 pid:29440
Jul 6 14:02:08 pid:29187
Jul 6 14:02:09 pid:29187
Jul 6 14:03:01 pid:29440
Jul 6 14:03:40 pid:29807
Jul 6 14:04:01 pid:29440
Jul 6 14:05:01 pid:29440
```

<br>

### Video: Making Sense out of the Data

Which of the following is a correct printout of a dictionary?

* **{'carrots':100, 'potatoes':50, 'cucumbers': 65}**
* **{50:'apples', 55:'peaches', 15:'banana'}**
* {55:apples, 55:peaches, 15:banana}
* {carrots:100, potatoes:50, cucumbers: 65}

> A dictionary stores key:value pairs.