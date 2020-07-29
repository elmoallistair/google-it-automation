# Managing Files and Directories

<br>

## Video: Working with Files

How can we check if a file exists inside a Python script?

* Renaming the file with os.rename.
* Creating the file with os.create.
* **Using the os.path.exists function.**
* Deleting the file with os.remove.

> The os.path.exists function will return True if the file exists, False if it doesn't.

<br>

## Video: More File Information

Some more functions of the os.path module include getsize() and isfile() which get information on the file size and determine if a file exists, respectively. In the following code snippet, what do you think will print if the file does not exist?

```
import os
file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
	print(os.path.isfile(file))
    print("File not found")
```

* file.dat<br>
1024
* False<br>
2048
* True<br>
512
* **False<br>
File not Found**

> Because the file does not exist, getsize() will never be called and our error message will be printed instead.

<br>

## Video: Directories

What's the purpose of the os.path.join function?

* **It creates a string containing cross-platform concatenated directories.**
* It creates new directories.
* It lists the file contents of a directory.
* It returns the current directory.

> By using os.path.join we can concatenate directories in a way that can be used with other os.path() functions.