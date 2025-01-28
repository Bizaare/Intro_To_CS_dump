# Author : Levi Yates
# Date   : 2022-09-26
# This program will count the number of voewls in a string.


def countVowels(inString):
    """Return the number of vowels in the string.
    Ignores case. Vowels are aeiou."""
    totalVowels = 0
    vowels = ["a", "e", "i", "o", "u"]
    
    for char in inString.lower():
            if char in vowels:
                totalVowels += 1

    return totalVowels




# This is my code after the functions
rawText = input("Please insert your text here: ")
print()
print
print("There are " + str(countVowels(rawText)) + " vowels in your text.")
