## Practice Quiz: Code that Crashes
* **Total points: 5**
* **Score: 100%**

<br>

### Question 1

Which of the following will let code run until a certain line of code is executed?

* **Breakpoints**
* Watchpoints
* Backtrace
* Pointers

> Breakpoints let code run until a certain line of code is executed.

<br>

### Question 2

Which of the following is NOT likely to cause a segmentation fault?

* Wild pointers
* Reading past the end of an array
* Stack overflow
* **RAM replacement**

> Segmentation fault is not commonly caused by a new RAM card in the system.

<br>

### Question 3

A common error worth keeping in mind happens often when iterating through arrays or other collections, and is often fixed by changing the less than or equal sign in our for loop to be a strictly less than sign. What is this common error known as?

* Segmentation fault
* backtrace
* The No such file or directory error
* **Off-by-one error**

> The Off-by-one bug, often abbreviated as OB1, frequently happens in computer programming when an iterative process iterates one time too many or too little.

<br>

### Question 4

A very common method of debugging is to add print statements to our code that display information, such as contents of variables, custom error statements, or return values of functions. What is this type of debugging called?

* Backtracking
* Log review
* **Printf debugging**
* Assertion debugging

> Printf debugging originated in name with using the printf() command in C++ to display debug information, and the name stuck. This type of debugging is useful in all languages.

<br>

### Question 5

When a process crashes, the operating system may generate a file containing information about the state of the process in memory to help the developer debug the program later. What are these files called?

* Log files
* **Core files**
* Metadata file
* Cache file

> Core files (or core dump files) record an image and status of a running process, and can be used to determine the cause of a crash.