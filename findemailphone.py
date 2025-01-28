# Author : Levi Yates
# Date   : 2022-10-17
# This program finds all email addresses and phone numbers in a

import re

Sentence = input("Input your text here: ")

pattern = '[^@\s]+@[^@\s]+'

matches = re.findall(pattern, Sentence)

print("matches = " + str(matches))

for match in matches:
    print("emails found: " + str(match))
    
pattern = r'[01]?[- .]?\(?[2-9]\d{2}\)?[- .]?\d{3}[- .]?\d{4}'

matches = re.findall(pattern, Sentence)

print("matches = " + str(matches))

for match in matches:
    print("phone numbers found: " + str(match))
                
