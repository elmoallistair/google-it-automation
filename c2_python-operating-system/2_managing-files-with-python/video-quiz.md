## Reading and Writing Files

<br>

### Video: Reading Files

What is the difference between the readline() and read() methods?

* The readline() method starts from the current position, while the read() method reads the whole file.
* The read() method reads a single line, the readline() method reads the whole file.
* The readline() method reads the first line of the file, the read() method reads the whole file.
* **The readline() method reads a single line from the current position, the read() method reads from the current position until the end of the file.**

> Both methods read from the current position. The readline() method reads one line, while read() reads until the end of the file.

<br>

### Video: Iterating through Files

Can you identify which code snippet will correctly open a file and print lines one by one without whitespace?

<ul>
    <li><pre>with open("hello_world.txt") as text:
        for line in text:
            print(line)</pre></li>
    <li><pre>with open("hello_world.txt") as text:
        for line in text:
            print(text)</pre></li>
    <li><pre>with open("hello_world.txt") as text:
        print(line)</pre></li>
    <li><pre><b>with open("hello_world.txt") as text:
        for line in text:
            print(line.strip())</b></pre></li>
</ul>

> Here, we are iterating line by line, and the strip() command is used to remove extra whitespace.

<br>

### Video: Writing Files

What happens to the previous contents of a file when we open it using "w" ("write" mode)?

* The new contents get added after the old contents.
* A new file is created and the old contents are kept in a copy.
* **The old contents get deleted as soon as we open the file.**
* The old contents get deleted after we close the file.

> When using write mode, the old contents get deleted as soon as the file is opened.

<br><hr><br>

## Managing Files and Directories

<br>

### Video: Working with Files

How can we check if a file exists inside a Python script?

* Renaming the file with os.rename.
* Creating the file with os.create.
* **Using the os.path.exists function.**
* Deleting the file with os.remove.

> The os.path.exists function will return True if the file exists, False if it doesn't.

<br>

### Video: More File Information

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

### Video: Directories

What's the purpose of the os.path.join function?

* **It creates a string containing cross-platform concatenated directories.**
* It creates new directories.
* It lists the file contents of a directory.
* It returns the current directory.

> By using os.path.join we can concatenate directories in a way that can be used with other os.path() functions.

<br><hr><br>

## Reading and Writing CSV Files

<br>

### Video: What is a CSV file?

If we have data in a format we understand, then we have what we need to parse the information from the file. What does parsing really mean?

* Reducing the logical size of a file to decrease disk space used and increase network transmission speed.
* Uploading a file to a remote server for later use, categorized by format
* **Using rules to understand a file or datastream as structured data.**
* Writing data to a file in a format that can be easily read later

> If we know the format of the data, we can separate it into understandable parts.

<br>

### Video: Reading CSV Files

Which of the following lines would correctly interpret a CSV file called "file" using the CSV module? Assume that the CSV module has already been imported.

* data=file.csv()
* file.opencsv()
* **data=csv.reader(file)**
* data=csv.open(file)

> The **reader()** function of the CSV module will interpret the file as a CSV.

<br>

### Video: Generating CSV

Which of the following must we do before using the csv.writer() function?

* Open the file with read permissions.
* Import the functools module.
* Import the argparse module.
* **Open the file with write permissions.**

> The file must be open, preferably using with open() as, and write permissions must be given.

<br>

### Video: Reading and Writing CSV Files with Dictionaries

DictReader() allows us to convert the data in a CSV file into a standard dictionary. DictWriter() \ allows us to write data from a dictionary into a CSV file. What’s one parameter we must pass in order for DictWriter() to write our dictionary to CSV format?

* The DictReader() function must be passed the CSV file
* The writerows() function requires a list of key
* The writeheader() function requires a list of keys
* **The fieldnames parameter of DictWriter() requires a list of keys**

> This will help DictWriter() organize the CSV rows properly.