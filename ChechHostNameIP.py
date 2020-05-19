#!/usr/bin/env python3

import socket
import sys
fileHandler = open("data.txt", "r")
print("Program Start")
line = fileHandler.readline()
if(line):
        while line:
        # Get next line from file
        # If line is empty then end of file reached
                ip2 =line.rstrip()
                try:
                    ip = socket.gethostbyname(ip2)
                except OSError as error:
                        print("Host not Find")
                else:
                        print("Host Name: {0} Ip: {1}".format(ip2, ip))
                line = fileHandler.readline()
else:
        print ("File Empty")

print ("Program end")
# Close Close
fileHandler.close()
