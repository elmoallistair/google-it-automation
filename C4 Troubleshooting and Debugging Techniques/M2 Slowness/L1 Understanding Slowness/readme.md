## Summary

* The general strategy for addressing slowness is to identify the `bottleneck`, could be CPU time, time spend reading data from disk or some other resource that limiting the overall performance.
  * If the problem is that your program needs more CPU time, you can close other running programs that you don't need right then. 
  * If the problem is that you don't have enough space on disk, you can uninstall applications that you don't use, or delete or move data that doesn't need to be on that disk. 
  * If the problem is that the application needs more network bandwidth, you can try stopping any other processes that are also using the network and so on
* When an application is accessing some data, the time spent retrieving that data will depend on where it's located. 
  * If it's a variable that's currently being used in a function, the data will be in the CPU's internal memory, and our program will retrieve it really fast. 
  * If the data is related to a running program but maybe not the currently executing function, it will likely be in RAM, and our program will still get to a pretty fast. 
  * If the data is in a file, our program will need to read it from disk, which is much slower than reading it from RAM, and worse than reading from disk, is reading information from over the network. 
  * In this case, we have a lower transmission speed, and we also need to establish the connection to the other endpoint to make the transmission possible, which adds to the total time needed to get to the data.  
* **Cache** stores data in a form that's faster to access than its original form
* **Memory leak** is memory which is no longer needed is not getting released
* When trying to figure out what's making a computer slow, the first step is to look into **when** the computer is slow.
  * If it's slow when starting up, it's probably a sign that there are too many applications configured to start on boot. In this case, fixing the problem is just a question of going through the list of programs that start automatically and disabling any that aren't really needed.
  * If instead the computer becomes sluggish after days of running just fine, and the problem goes away with a reboot, it means that there's a program that's keeping some state while running that's causing the computer to slow down.
  * If a program like this stays running for many days, the data might grow so much that reading it becomes slow and the computer runs out of RAM. This is almost certainly a bug in the program. And the ideal solution for a problem like this is to change the code so that it frees up some of the memory used. If you don't have access to the code, another option is to schedule a regular restart to mitigate both the slow program and your computer running out of RAM. 