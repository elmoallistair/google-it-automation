#! /usr/bin/env python3

# Google IT Automation with Python Professional Certificate
# Elmo Allistair
# 11 Agu 2020

import os
import requests

'''
List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.
Hint: Use os.listdir() method for this, which returns a list of all files and directories in the specified path.
'''
dir = "/data/feedback/"
for file in os.listdir("/data/feedback/"): 
    '''
    You should now have a list that contains all of the feedback files from the path /data/feedback. 
    Traverse over each file and, from the contents of these text files, create a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively.
    '''
    format = ["title","name","date","feedback"]

    '''
    Now, you need to have a dictionary with keys and their respective values (content from feedback files). 
    This will be uploaded through the Django REST API.
    '''
    content = {}
    
    with open('{}/{}'.format(dir,file), 'r') as txtfile:
        counter = 0
        for line in txtfile:
            line = line.replace("\n", "")
            content[format[counter]] = line.strip('\n')
            counter += 1
    
    '''
    Use the Python requests module to post the dictionary to the company's website. 
    Use the request.post() method to make a POST request to http://<corpweb-external-IP>/feedback. 
    Replace <corpweb-external-IP> with corpweb's external IP address.
    '''
    response = requests.post("http://35.225.95.53/feedback/",json = content)

    '''
    You can print the status_code and text of the response objects to check out what's going on. 
    You can also use the response status_code 201 for created success status response code that indicates the request has succeeded.
    '''
    if not response.ok:
        raise Exception("POST failed! | Status code: {} | File: {}".format(response.status_code, file))
    print("Feedback added!")