## Summary

* We should always start by writing clear code that does what it should, and only try to make it faster if we realize that it's not fast enough
* Trying to optimize every second out of a script is probably not worth your time
* If we want our code to finish faster, we need to make our computer do less work
* **Profiler** is a tool that measures the resources that our code is using, giving us a better understanding of what's going on
* **Expensive actions** is those that can take a long time to complete
* **Lists** is sequences of elements. We can add, remove or modify the elements in them, and we can iterate through the whole list to operate on each of the elements.
* **Dictionaries** store key-value pairs. We add data by association a value to a key, and then we retrieve a value by looking up a specific key
* If you need to access elements by position, or will always iterate through all the elements, use a list to store them
* If we need to look up the elements using a key, we'll use a dictionary
* If you do an expensive operation inside a loop, you multiply the time it takes to do the expensive operation by the amount of times you repeat the loop
* Make sure that the list of elements that you're iterating through is only as long as you really need it to be
* Another thing to remember about loops is to break out the loop once you've found what you were looking for
* Three different values in `time` command:
  * **real**, the amount of actual time that it took to execute the command
  * **user**, the time spent doing operations in the user space
  * **sys**, the time spent doing system-level-operation