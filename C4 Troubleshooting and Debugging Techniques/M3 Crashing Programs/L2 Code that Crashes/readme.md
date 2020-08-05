## Summary

* Accessing invalid memory means that the process tried to access a portion of the system's memory that wasn't assigned to it.
* **Pointers**: The variables that store memory adresses
* **Undefined behavior**: The code is doing something that's not valid in the programming language
* **Valgrind**: A very powerful tool that can tell us if the code is doing any invalid operations, no matter if it crashes or not
* **Traceback**: Shows the line of different functions that were being executed when the problem happened
* **Core files** store all the information related to the crash so that we, or someone else, can debug what's going on