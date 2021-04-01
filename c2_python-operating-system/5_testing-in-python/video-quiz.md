## Simple Tests

<br>

### Video: What is testing?

When you test software, what are you really looking for?

* Loops
* Conditionals
* Modules
* **Defects**

> You want to find errors and defects when testing software. 

<br>

### Video: Manual Testing and Automated Testing

The advantage of running automated tests is that they will always get the same expected ___ if the software code is good.

* Command line arguments
* Parameters
* **Results**
* Interpreters

> Automatic tests will always get the same expected result if the software code is good.

<br><br>

# Unit Tests

<br>

### Video: Unit Tests

An important characteristic of a unit test is ___. 

* **Isolation.**
* A production environment
* An external database
* Automation.

> Unit tests test the piece of code they target.

<br>

### Video: Writing Unit Tests in Python

What module can you load to use a bunch of testing methods for your unit tests?

* TestCase
* **unittest**
* assertEqual
* Test

> This module provides a TestCase class with a bunch of testing methods.

<br>

### Video: Edge Cases

Which of the following would NOT be considered as an edge case when testing a software's input for a user's first and last name?

* -100
* **Jeffrey**
* Ben05
* 0

> A user's name with only letters is expected.

<br>

### Video: Additional Test Cases

Which of the following is NOT an advantage of running an automatic unit test in a suite for a single function?

* Efficiency
* **Creating multiple test scripts**
* Creating one script for multiple test cases
* Reusable test cases

> It’s harder to manage multiple test scripts.

<br><hr><br>

## Other Test Concepts

<br>

### Video: Black Box vs. White Box

Which of the following is descriptive of a black-box test case?

* The tester is familiar with the code.
* The code is open-source.
* **Code is opaque.**
* Tests are created alongside the code development.

> Black-box tests have no knowledge of the code.

<br>

### Video: Other Test Types

Running a piece of software code as-is to see if it runs describes what type of testing?

* Load test
* **Smoke test**
* Integration test
* Regression test

> Keep it up! This test finds out if the program can run in its basic form before undergoing more refined test cases.

<br><hr><br>

## Errors and Exceptions

<br>

### Video: The Try-Except Construct

When a try block is not able to execute a function, which of the following return examples will an exception block most likely NOT return?

* Empty String
* Zero
* **Error**
* Empty List

> An exception is not meant to produce an error, but to bypass it. 

<br>

### Video: Raising Errors

What keyword can help provide a reason an error has occurred in a function?

* return
* **assert**
* raise
* minlen

> This keyword is used to produce a message when a conditional is false.

<br>

### Video: Testing for Expected Errors

When using the assertRaises method, what is passed first?

* **Error**
* Function name
* Parameters
* Conditional

> Way to go! The expected error is passed first.