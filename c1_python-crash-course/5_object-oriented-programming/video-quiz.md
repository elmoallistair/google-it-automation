## Object-oriented Programming

<br>

### Video: What is Object-oriented programming?

Attributes are characteristics associated with a type. Methods are:

* Lists associated with a type
* Instances of a class
* **Functions associated with a type**
* Characteristics associated with a type

> A method defines what you do with an object.

<br>

### Video: Classes and Objects in Python

You want to find more information about the integer (int) class. What’s the best way to do this?

* **Use the command help(int)**
* Use the command type(int)
* Type ‘q’
* Use the len() function

> Using the help command can be useful for finding quick documentation about the methods in a class.

<br>

### Video: Defining New Classes

Fill in the blanks in the code to make it print a poem.

```
class Flower:
  color = 'unknown'

rose = Flower()
rose.color = 'Red'

violet = Flower()
violet.color = 'Blue'

this_pun_is_for_you = """One day we'll cruise down
Blood Gulch avenue
It's red versus red,
and blue versus blue
It's I against I,
and me against you
Violets are blue, roses are red,      
living like this we were already dead
Hop in my car,
it don't have any doors
It's built like a cat,
It lands on all fours
My car's like a puma,
it drives on all fours
Red versus red
Blue versus blue."""

print("Roses are {},".format(rose.color))
print("Violets are {},".format(violet.color))
print(this_pun_is_for_you) 
```

Output:

```
Roses are Red,
Violets are Blue,
One day we'll cruise down
Blood Gulch avenue
It's red versus red,
and blue versus blue
It's I against I,
and me against you
Violets are blue, roses are red,      
living like this we were already dead
Hop in my car,
it don't have any doors
It's built like a cat,
It lands on all fours
My car's like a puma,
it drives on all fours
Red versus red
Blue versus blue.
```

<br><hr><br>

## Classes and Methods

<br>

### Video: Instance Methods

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

<br>

### Video: Constructors and Other Special Methods

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

<br>

### Video: Documenting Functions, Classes, and Methods (Optional)

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

<br><hr><br>

## Code Reuse

<br>

### Video: Inheritance

Let’s create a new class together and inherit from it. Below we have a base class called Clothing. Together, let’s create a second class, called Shirt, that inherits methods from the Clothing class. Fill in the blanks to make it work properly.

```
class Clothing:
  material = ""
  def __init__(self,name):
    self.name = name
  def checkmaterial(self):
	  print("This {} is made of {}".format(self.name,self.material))
			
class Shirt(Clothing):
  material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()
```

Output:

```
This Polo is made of Cotton
```

<br>

### Video: Composition

Let’s expand a bit on our Clothing classes from the previous in-video question. Your mission: Finish the "Stock_by_Material" method and iterate over the amount of each item of a given material that is in stock. When you’re finished, the script should add up to 10 cotton Polo shirts.

```
class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  
  def __init__(self,name):
    material = ""
    self.name = name
    
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  
  def Stock_by_Material(self, material):
    count = 0
    n = 0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n += 1
    return count

class shirt(Clothing):
  material="Cotton"

class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)
```

Output:

```
10
```

<br>

### Video: Python Modules

Let’s say we want to use the Keras deep learning module. Upon running the script, an error is printed stating the Keras module could not be found. What might we have missed?

* We need to initialize the timedelta class
* We need to define Keras functions
* We need to define Keras attributes
* **We need to import the Keras module**

> We must use the import keyword to import the module before it can be used.
