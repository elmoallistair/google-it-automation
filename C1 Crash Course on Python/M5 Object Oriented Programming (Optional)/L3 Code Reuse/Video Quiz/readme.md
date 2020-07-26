# Code Reuse

<br>

## Video: Inheritance

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

## Video: Composition

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

## Video: Python Modules

Let’s say we want to use the Keras deep learning module. Upon running the script, an error is printed stating the Keras module could not be found. What might we have missed?

* We need to initialize the timedelta class
* We need to define Keras functions
* We need to define Keras attributes
* **We need to import the Keras module**

> We must use the import keyword to import the module before it can be used.