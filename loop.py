# Author : Levi Yates
# Date   : 2022-09-19
# Loop.py demonstrating loops

## [[- IMPORTS

import time

## -]]



# Count from 5 to 100 by 5's
##for i in range(5, 101, 5):
##    print("i = " + str(i))

# Count from 120 to -40 by 2's
##for temperature in range(120, -41, -2):
##    print("temperature = " + str(temperature))


# Convert between Fahrenheit to Celcius equivalents
##print("This program prints Fahrentheit to Celcius equivalents.")
##print("Starting at 212F down to -60F.")
##print()
##for F in range (212, -61, -1):
##    C = (F - 32) * 5/9
####    print("F = " + str(F) + " C = " + str(C))
##    print(format(F, '3.0f') + "\u00B0F  " + format(C, '5.2f') + "\u00B0C")

##print("Latin character set.")
##for i in range(65, 123):
####    print(chr(i))
##    print(chr(i), end="  ")
##
##print()
##
##print("Latin character set.")
##for i in range(0x41, 0x7B):
####    print(chr(i))
##    print(chr(i), end="  ")
##
##print()
##
##print("Cryillic character set.")
##for i in range(0x400, 0x500):
##    print(chr(i), end= "  ")
##print()

##print("Emoticons")
##for i in range(0x1F600, 0x1F650):
####    print(chr(i))
##    print(chr(i), end="  ")

##i = 0
##while i <= 10:
##    print("i = " + str(i))
##    i = i + 0.25

##print("Making a multiplication table...")
##rowStop = int(input("How many rows?    "))
##colStop = int(input("How many columns? "))
##
##print("Starting...")
##startTime = time.time()
##print("Start time = " + str(startTime))
##
##
##for row in range(1, rowStop + 1):
##    for col in range(1, colStop + 1):
##        multResult = row * col
####        print("row = " + str(row) + "  col = " + str(col)
####              + "  r = " + str(multResult))
##
##        print(format(multResult, '4.0f'), end="  ")
##    print()
##
##print("Stopped...")
##stopTime = time.time()
##print("Stop time = " + str(stopTime))
##
##elapsedTime = stopTime - startTime
##print("Time to execute = " + str(elapsedTime))
##
##print("Done...")

print("This program adds up all the numbers from 1 to 100 inclusive.")
print("answer = 1 + 2 + 3 + 4 + ... + 97 + 98 + 99 + 100")



total = 0
for i in range(1, 101):
    total = total + i
   ## print("i = " + str(i) + "  total = " + str(total))

print()
print("Answer is = " + str(total))
