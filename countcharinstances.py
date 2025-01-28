# Author : Levi Yates
# Date   : 2022-10-10
# This program will count each character in a string.



def countCharacters(inString):
    counters = {}
    for i in range(0x20, 0x7F):
        counters[chr(i)] = 0
    for char in inString:
        counters[char] += 1
    for char, count in counters.items():
        if count > 0:
            print(f"{char}: {count}")
        
inputText = input("Insert your text here: ")
countCharacters(inputText)
