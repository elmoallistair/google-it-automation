# Classes and Methods

## Instance Methods

Create a Dog class with dog_years based on the Piglet class shown before (one human year is about 7 dog years).

```
class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7
    
fido = Dog()
fido.years = 3
print(fido.dog_years())
```

Output:

```
21
```

## Constructors and Other Special Methods

Want to see this in action? In this code, there's a Person class that has an attribute name, which gets set when constructing the object. Fill in the blanks so that 1) when an instance of the class is created, the attribute gets set correctly, and 2) when the greeting() method is called, the greeting states the assigned name.

```
class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return f"hi, my name is {self.name}"

# Create a new instance with a name of your choice
some_person = Person("Elmo")  
# Call the greeting method
print(some_person.greeting())
```

Output:

```
hi, my name is Elmo
```

## Documenting Functions, Classes, and Methods (Optional)

Remember our Person class from the last video? Let’s add a docstring to the greeting method. How about, “Outputs a message with the name of the person”.

```
class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with the name of the person"""
    print("Hello! My name is {name}.".format(name=self.name)) 

help(Person)
```

Output:

```
Help on class Person in module submission:

class Person(builtins.object)
 |  Methods defined here:
 |  
 |  __init__(self, name)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  greeting(self)
 |      Outputs a message with the name of the person
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