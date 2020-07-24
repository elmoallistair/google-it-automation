# Processing Log Files

## Filtering Log Files with Regular Expressions

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

## Making Sense out of the Data

Which of the following is a correct printout of a dictionary?

* **{'carrots':100, 'potatoes':50, 'cucumbers': 65}**
* **{50:'apples', 55:'peaches', 15:'banana'}**
* {55:apples, 55:peaches, 15:banana}
* {carrots:100, potatoes:50, cucumbers: 65}

> A dictionary stores key:value pairs.