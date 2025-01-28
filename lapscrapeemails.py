# Author : Levi Yates
# Date   : 2022-11-10
# This is a highly legal program that scrapes emails from websites!

import re
import os
import urllib.request
import ssl # Needed for https

# Needed for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
print("Reading the SCTCC department directory...")
url = 'https://www.sctcc.edu/contact-us'
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 '\
        '(KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(url + '/', context=ctx)

print("Opening output text file for writing...")
file = open("email_addresses.txt", "a")
print("These email addresses were found in the text...")
print()
longline = ""

emailcount = 0


for line in response:
    line = line.decode('utf-8')
    longline += line

    pattern = '(mailto:)([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
    matches = re.findall(pattern, line)
    
    for match in matches:
        emailcount += 1
        print(str(match[1]))
        file.write(str(match[1]) + '\n')

file.close()


