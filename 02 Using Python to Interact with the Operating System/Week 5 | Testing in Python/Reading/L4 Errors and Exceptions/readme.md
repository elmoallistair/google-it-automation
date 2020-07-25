# Handling Errors Cheat-Sheet

Raise allows you to throw an exception at any time.

* https://docs.python.org/3/tutorial/errors.html#raising-exceptions

Assert enables you to verify if a certain condition is met and throw an exception if it isn’t.

* https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement
* https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python

The standard library documentation is kind of unclear. Basically `assert <something false>` will raise AssertionError, which the caller may need to handle.

In the try clause, all statements are executed until an exception is encountered.

* https://docs.python.org/3/tutorial/errors.html#handling-exceptions

Except is used to catch and handle the exception(s) that are encountered in the try clause.

* https://docs.python.org/3/library/exceptions.html#bltin-exceptions

Other interesting Exception handling readings:

* https://doughellmann.com/blog/2009/06/19/python-exception-handling-techniques/