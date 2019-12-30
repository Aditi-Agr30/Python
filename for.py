#!usr/bin/python3

import subprocess,time,webbrowser,os,sys

#l1 = [12,30,100]   Dead code
#Dynamic input
#dyn_input=(sys.argv[1:])
"""sum = 0
for i in dyn_input:
        sum = sum+int(i)
        print("Element added",i)
        time.sleep(1)

print("Sum of elements: " , sum)"""

file=open("elements.txt","r")
line=file.read()
line.split(",")
print(line.split(","))
total=sum([int(i)  for i in line.split(',')])
print("Sum of elements: ",total)

