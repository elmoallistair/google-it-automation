## Practice Quiz: Deploying Puppet Locally
* **Total points: 5**
* **Score: 100%**

<br>

### Question 1

Puppet evaluates all functions, conditionals, and variables for each individual system, and generates a list of rules for that specific system. What are these individual lists of rules called?

* Manifests
* Dictionaries
* **Catalogs**
* Modules

> The catalog is the list of rules for each individual system generated once the server has evaluated all variables, conditionals, and functionals in the manifest and then compared them with facts for each system.

<br>

### Question 2

After we install new modules that were made and shared by others, which folder in the module's directory will contain the new functions and facts?

* files
* manifests
* **lib**
* templates

> New functions added after installing a new module can be found in the lib folder in the directory of the new module.

<br>

### Question 3

What file extension do manifest files use?

* .cfg
* .exe
* **.pp**
* .man

> Manifest files for Puppet will end in the extension .pp.

<br>

### Question 4

What is contained in the metadata.json file of a Puppet module?

* Manifest files
* **Additional data about the module**
* Configuration information
* Pre-processed data

> Metadata is data about data, and in this case, often takes the form of installation and compatibility information.

<br>

### Question 5

What does Puppet syntax dictate we do when referring to another resource attribute?

* Enter the package title before curly braces
* Follow the attribute with a semicolon
* **Capitalize the attribute**
* Type the attribute in lowercase

> When defining resource types, we write them in lowercase, then capitalize them when referring to them from another resource attribute.