#!/usr/bin/env python3

# Import all the Python modules
import re
import sys
import operator
import csv

# Initialize two dictionaries: 
# one for the number of different error messages 
# and another to count the number of entries for each user (splitting between INFO and ERROR).
error = {}
per_user = {}

# Parse through each log entry in the syslog.log file by iterating over the file.
with open("syslog.log") as f:
	for line in f:
		username = re.search(r"\((.*)\)",line).group(1)
		user_count = {'INFO': 0, 'ERROR': 0}
		if username not in per_user:
			per_user[username] = user_count
		# For each log entry, you'll have to first check if it matches the INFO or ERROR message formats. You should use regular expressions for this.
		# When you get a successful match, add one to the corresponding value in the per_user dictionary.
		if "INFO" in line:
			per_user[username]['INFO'] += 1

	    # If you get an ERROR message, add one to the corresponding entry in the error dictionary by using proper data structure.
		elif "ERROR" in line:
			err_msg = re.search(r"ERROR (.*) ",line).group(1)
			if err_msg not in error:
				error[err_msg] = 0
			error[err_msg] += 1
			per_user[username]['ERROR'] += 1

# print(error)
# print(per_user)

# After you've processed the log entries from the syslog.log file, you need to sort both the per_user and error dictionary before creating CSV report files.
error_sorted = []
user_sorted = []

# The error dictionary should be sorted by the number of errors from most common to least common.
for error, count in sorted(error.items(), key=lambda item: item[1],reverse=True):
    error_sorted.append([error, count])

# The user dictionary should be sorted by username.
for username in sorted(per_user.keys()):
    user_sorted.append([username, per_user[username]["INFO"], per_user[username]["ERROR"]])

# Insert column names as ("Error", "Count") at the zero index position of the sorted error dictionary. 
error_sorted.insert(0,["Error","Count"])
# And insert column names as ("Username", "INFO", "ERROR") at the zero index position of the sorted per_user dictionary.
user_sorted.insert(0,["Username","INFO","ERROR"])

# After sorting these dictionaries, store them in two different files: error_message.csv and user_statistics.csv.
with open("error_message.csv","w") as error_msg_file:
	writer = csv.writer(error_msg_file)
	writer.writerows(error_sorted)
	error_msg_file.close()

with open("user_statistics.csv","w") as user_statistics_file:
	writer = csv.writer(user_statistics_file)
	writer.writerows(user_sorted)
	user_statistics_file.close()

# print(error_sorted)
# print(user_sorted)