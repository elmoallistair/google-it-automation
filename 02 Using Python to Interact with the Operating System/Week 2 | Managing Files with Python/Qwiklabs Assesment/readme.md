## Qwiklabs Assessment: Handling Files

<hr>

### Introduction

For this lab, imagine you are an IT Specialist at a medium-sized company. The Human Resources Department at your company wants you to find out how many people are in each department. You need to write a Python script that reads a CSV file containing a list of the employees in the organization, counts how many people are in each department, and then generates a report using this information. The output of this script will be a plain text file.

You will have 90 minutes to complete this lab

**Passed 100%**

<hr>

### Accessing the virtual machine

**Option 2: OSX and Linux users: Connecting to your VM via SSH**

```
chmod 600 ~/Downloads/qwikLABS-XXXXX.pem
ssh -i ~/Downloads/qwikLABS-XXXXX.pem username@External Ip Address
```

### Prerequisites

```
cd data
ls
cat employees.csv
cd ~/scripts
nano generate_report.py
```

### Convert employee data to dictionary

**`File: generate_report.py`**
```
#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
  employee_list = []
  for data in employee_file:
    employee_list.append(data)
  return employee_list

employee_list = read_employees('/home/<username>/data/employees.csv')
print(employee_list)
```

```
chmod +x generate_report.py
./generate_report.py 
```

The list employees_list within the script should return the list of dictionaries as shown below

![img](https://cdn.qwiklabs.com/34yJi4Dtn9hrTnj7iVRtpdg69SxaIK2ZaijqJipbqJI%3D)

### Process employee data

```
nano generate_report.py
```

**`File: generate_report.py`**
```
#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
  employee_list = []
  for data in employee_file:
    employee_list.append(data)
  return employee_list

def process_data(employee_list):
  department_list = []
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])
  
  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)
  return department_data

employee_list = read_employees('/home/<username>/data/employees.csv')
print(employee_list)

dictionary = process_data(employee_list)
print(dictionary)
```

```
./generate_report.py
```

This should return a dictionary in the format `department: amount`, as shown below

![img](https://cdn.qwiklabs.com/GEZ0BrlPKu2ecgNF%2FV8C%2FGZSUgFtWlZyS9jN6wXoa50%3D)

### Generate a report

```
nano generate_report.py
```

**`File: generate_report.py`**
```
#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
  employee_list = []
  for data in employee_file:
    employee_list.append(data)
  return employee_list

def process_data(employee_list):
  department_list = []
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])
  
  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)
  return department_data

def write_report(dictionary, report_file):
  with open(report_file, "w+") as f:
    for k in sorted(dictionary):
      f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()

employee_list = read_employees('/home/<username>//data/employees.csv')
print(employee_list)

dictionary = process_data(employee_list)
print(dictionary)

write_report(dictionary, '/home/<username>/data/report.txt')
```

```
./generate_report.py
cd ~/data
ls
cat report.txt
```

The report file should be similar to the below image.

![img](https://cdn.qwiklabs.com/biV9qHPyqAYfGVa246u5rZGbScQ1L3PZ%2BrTZVmCwCHc%3D)