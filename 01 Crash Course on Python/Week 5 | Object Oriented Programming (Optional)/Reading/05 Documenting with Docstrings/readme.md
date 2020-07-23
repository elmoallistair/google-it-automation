# Documenting with Docstrings

The Python **help** function can be super helpful for easily pulling up documentation for classes and methods. We can call the **help** function on one of our classes, which will return some basic info about the methods defined in our class:

```
>>> class Apple:
...     def __init__(self, color, flavor):
...         self.color = color
...         self.flavor = flavor
...     def __str__(self):
...         return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
... 
>>> help(Apple)
Help on class Apple in module __main__:

class Apple(builtins.object)
 |  Methods defined here:
 |  
 |  __init__(self, color, flavor)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __str__(self)
 |      Return str(self).
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
```


We can add documentation to our own classes, methods, and functions using docstrings. A **docstring** is a short text explanation of what something does. You can add a docstring to a method, function, or class by first defining it, then adding a description inside triple quotes. Let's take the example of this function:

```
>>> def to_seconds(hours, minutes, seconds):
...     """Returns the amount of seconds in the given hours, minutes and seconds."""
...     return hours*3600+minutes*60+seconds
...
```

We have our function called to_seconds on the first line, followed by the docstring which is indented to the right and wrapped in triple quotes. Last up is the function body. Now, when we call the help function on our to_seconds function, we get a handy description of what the function does:

```
>>> help(to_seconds)
Help on function to_seconds in module __main__:

to_seconds(hours, minutes, seconds)
    Returns the amount of seconds in the given hours, minutes and seconds.
```

Docstrings are super useful for documenting our custom classes, methods, and functions, but also when working with new libraries or functions. You'll be extremely grateful for docstrings when you have to work with code that someone else wrote!