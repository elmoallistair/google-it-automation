## Summary

* To find the root cause of a crashing application, we'll want to look at all available logs, figure out what changed, trace the system or library calls the program makes, and create the smallest possible reproduction case
* **Wrapper** is a function or program that provides a compatibility layer between two functions or programs, so they can work well together
* **Watchdog** is a process that checks whether a program is running, and when it's not, starts the program again
* When you report a bug make sure you include as much information as possible, answer the question:
  * What were you trying to do?
  * What were the steps you followed?
  * What did you expect to happen?
  * What was the actual outcome?