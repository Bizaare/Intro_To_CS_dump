# Author : Levi Yates
# Date   : 2022-10-31
# Dictionary data structure examples
# Dictionaries in Python are also known as associative arrays or hash tables.

color = {"red":0.43, "blue":2, "green":3, "blue":88, "Red":99}

print(color)
print()

print(color.get("blue"))
print()

print(color.get("green"))
print()

print(color.get("purple"))
print()

print(color.get("red"))
print(color.get("Red"))

for item in color:
    print(item, "$" + str(color.get(item)))

print()
print("Returns a view of the key value pairs.")
print(color.items())

print()
print("Returns a view of the values.")
print(color.values())

# 0 1 2 3 4 5 6 7 8 9

englishDictionary = {"zero":"cero", "one":"uno", "two":"dos", "three":"tres", "four":"cuatro", "five":"cinco", "six":"seis", "seven":"siete", "eight":"ocho", "nine":"nueve"}

print(englishDictionary)
print()

for english_word in englishDictionary:
    print(english_word, englishDictionary.get(english_word))

print()
inputString = input("Give me a phone number: ").lower()

english_phone_array = inputString.split(" ")
print(english_phone_array)

for english_word in english_phone_array:
    print(englishDictionary.get(english_word))

print()

enDictionary = {"zero":("cero", 0), "one":("uno", 1)}
print(enDictionary)
print(enDictionary.get("one")[0])
print()
