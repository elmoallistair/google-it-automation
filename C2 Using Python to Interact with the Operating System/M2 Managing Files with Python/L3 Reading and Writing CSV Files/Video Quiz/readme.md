# Reading and Writing CSV Files

<br>

## Video: What is a CSV file?

If we have data in a format we understand, then we have what we need to parse the information from the file. What does parsing really mean?

* Reducing the logical size of a file to decrease disk space used and increase network transmission speed.
* Uploading a file to a remote server for later use, categorized by format
* **Using rules to understand a file or datastream as structured data.**
* Writing data to a file in a format that can be easily read later

> If we know the format of the data, we can separate it into understandable parts.

<br>

## Video: Reading CSV Files

Which of the following lines would correctly interpret a CSV file called "file" using the CSV module? Assume that the CSV module has already been imported.

* data=file.csv()
* file.opencsv()
* **data=csv.reader(file)**
* data=csv.open(file)

> The **reader()** function of the CSV module will interpret the file as a CSV.

<br>

## Video: Generating CSV

Which of the following must we do before using the csv.writer() function?

* Open the file with read permissions.
* Import the functools module.
* Import the argparse module.
* **Open the file with write permissions.**

> The file must be open, preferably using with open() as, and write permissions must be given.

<br>

## Video: Reading and Writing CSV Files with Dictionaries

DictReader() allows us to convert the data in a CSV file into a standard dictionary. DictWriter() \ allows us to write data from a dictionary into a CSV file. What’s one parameter we must pass in order for DictWriter() to write our dictionary to CSV format?

* The DictReader() function must be passed the CSV file
* The writerows() function requires a list of key
* The writeheader() function requires a list of keys
* **The fieldnames parameter of DictWriter() requires a list of keys**

> This will help DictWriter() organize the CSV rows properly.