#!/usr/bin/env python3

import csv
import datetime
import requests

# def get_file_lines(url):
def download_file(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_same_or_newer(data, start_date):
    """Returns the employees that started on the given date, or the closest one."""
    # We want all employees that started at the same date or the closest newer
    # date. To calculate that, we go through all the data and find the
    # employees that started on the smallest date that's equal or bigger than
    # the given start date.
    min_date = datetime.datetime.today()
    min_date_employees = []
    for row in data: 
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')

        # If this date is smaller than the one we're looking for,
        # we skip this row
        if row_date < start_date:
            continue

        # If this date is smaller than the current minimum,
        # we pick it as the new minimum, resetting the list of
        # employees at the minimal date.
        if row_date < min_date:
            min_date = row_date
            min_date_employees = []

        # If this date is the same as the current minimum,
        # we add the employee in this row to the list of
        # employees at the minimal date.
        if row_date == min_date:
            min_date_employees.append("{} {}".format(row[0], row[1]))

    return min_date, min_date_employees

def list_newer(data, start_date):
    while start_date < datetime.datetime.today():
        start_date, employees = get_same_or_newer(data, start_date)
        print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))

        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)

def main():
    start_date = get_start_date()
    FILE_URL = "https://storage.googleapis.com/gwg-hol-assets/gic215/employees-with-date.csv"
    data = download_file(FILE_URL) # Hint 1. Download the file only once from the URL.
    reader = csv.reader(data[1:])
    data_list = list(reader)
    data_list.sort(key = lambda x: x[3]) # Hint 2. To sort the data by start_date and then go date by date.
    list_newer(data_list, start_date) 

if __name__ == "__main__":
    main()

"""
# Testing in my local machine, many improvement can be more applied

Before: 
        1st attempt | 2nd attempt | 3rd attempt
real    0m46,007s   | 1m1,561s    | 0m53,076s
user    0m7,663s    | 0m9,278s    | 0m9,166s
sys     0m0,362s    | 0m0,426s    | 0m0,405s

After:
        1st attempt | 2nd attempt | 3rd attempt
real    0m1,770s    | 0m3,155s    | 0m3,642s
user    0m1,216s    | 0m0,311s    | 0m0,284s
sys     0m0,045s    | 0m0,038s    | 0m0,045s
"""