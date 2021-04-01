#!/usr/bin/env python3
# just code for testing

content = {}
format = ["title","name","date","feedback"]

with open('001.txt', 'r') as txtfile:
    counter = 0
    for line in txtfile:
        line = line.replace("\n", "")
        content[format[counter]] = line.strip('\n')
        counter += 1
        print(counter, line)

print(lst)
print(content)
