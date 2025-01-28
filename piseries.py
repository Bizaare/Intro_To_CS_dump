# Author : Levi Yates
# Date   : 2022-09-19
# This program will calculate Pi out to the 10,000,000th term.


# Hints:
# Pi/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 ...


total = 0

signThing = 1
for i in range(1, 10000000, 2):
    total = total + signThing * 1 / i
    signThing = signThing * -1

print(total * 4)

   
 
