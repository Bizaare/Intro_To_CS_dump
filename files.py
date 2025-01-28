# Author : Levi Yates
# Date   : 2022-11-07
# Examples of programming that demonstrates file usage.

import os
import urllib.request
import ssl # Needed for https
import re

##name = input("What is your name? ")
##color = input("What is your favorite color? ")
##
##print("Your name is " + name)
##print("Your favorite color is " + color)
##
### Create a text file.
##file = open("personalinfo.txt", "a")
##
##file.write(name + ", ")
##file.write(color + "\n")
##
##file.close()
##
##path = os.path.realpath("personalinfo.txt")
##print(path)

# Open a file for reading
file = open("monthtemperatures.csv", "r")
contents = file.read()

file.close()

print(contents)

temperatures = contents.split(",")
print(temperatures)

for temp in temperatures:
    print(float(temp))

print()
file = open("personalinfo.txt", "r")
namescolors = file.read()
file.close()
print(namescolors)

# working website: cst.ridgewater.edu
# working https website cnet.com

print("Please include https:// or https:// before the web addess")
print("Example > https://cnet.com")

website_name = input("Enter a website name: ")

# Needed for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

response = urllib.request.urlopen(website_name + '/',context=ctx)

longline = ""
linecount = 0
electionWordCount = 0

print(response)

for line in response:
    line = line.decode('utf-8') # Decoding the binary data as text.
    line = line.lower()

    longline += line
    linecount += 1

    electionWordFind = line.find("election")

    if electionWordFind >= 0:
        electionWordCount += 1
        print("ELECTION found on line: " + str(linecount))

print("Total lines of html code = " + str(linecount))
print("Number of times 'ELECTION' found = " + str(electionWordCount))

electionPattern = '(election)'
electionMatches = re.findall(electionPattern, longline)
numMatches = 0
for match in electionMatches:
    #print(match)
    numMatches += 1

print("Total number of times 'election' found = " + str(numMatches))
