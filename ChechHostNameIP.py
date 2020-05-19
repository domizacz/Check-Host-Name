#!/usr/bin/env python3

import socket
import sys
fileHandler = open("data.txt", "r")
print("Program Start")
line = fileHandler.readline()
while line:
# Get next line from file
# If line is empty then end of file reached
        ip2 =line.rstrip()
        ip = socket.gethostbyname(ip2)
        print("Host Name: {0} Ip: {1}".format(ip2, ip))
        line = fileHandler.readline()

print ("Program end")
# Close Close
fileHandler.close()
