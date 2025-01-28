## Author : Levi Yates
## Date: 2022/10/24
## General list usage examples
##
##words = ["baseball", "stadium", "hot dogs", "beer", "bat", "umpire", "beer"]
##
##print(words)
##print(words[2])
##print(words[0])
##print(words[-1])
##
##print()
##print(len(words))
##
##print()
##for i in range(0, len(words)):
##    print(words[i])
##
##print()
##print("Shorthand method...")
##for word in words:
##    print(word)
##
##print()
##print(words.index("beer"))
##print(words.index("mound"))
##
##print()
##words.append("fans")
##words.append("pitcher")
##
##print()
##print("Shorthand method...")
##for word in words:
##    print(word)
##
##words.insert(3, "players")
##print()
##print("Shorthand method...")
##for word in words:
##    print(word)
##
##words.insert(-2, "diamond")
##print()
##print("Shorthand method...")
##for word in words:
##    print(word)
##
##print()
##print("Returning a count...")
##print(words.count("stadium"))
##print(words.count("peanuts"))
##print(words.count("beer"))
##
##
##wordToBeFound = "mound"
##if words.count(wordToBeFound) > 0:
##    print("Index in list is: " + str(words.index(wordToBeFound)))
##
##else:
##    print("Word is not in the list.")
##
##
##print()
##words.sort()
##print(words)
##words.reverse()
##print(words)
##
##latin = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam sit amet enim sollicitudin, ullamcorper dui nec, fringilla nisl. Fusce bibendum elit eget magna suscipit, quis placerat nunc interdum."
##
##print(latin)
##splitup = latin.split(" ")
##print(splitup)
##
##print()
##
##temperatures = "24, 29, 41, 58, 69, 79, 83, 80, 72, 58, 41, 27"
##monthHiTemps = temperatures.split(", ")
##print(monthHiTemps)
##for temp in monthHiTemps:
##    print(temp)
##
##trees = ["oak", "ash", "elm", "pine"]
##print(trees)
##
##removed_item = trees.pop()
##print(removed_item)
##print(trees)
##trees.append("sycamore") # append can be thought of as
##trees.append("birch")   # a "push" when dealing with a stack.
##print(trees)
##removed_item = trees.pop()
##print(trees)
##
##
##numbers_list = []
##
##while True:
##    user_input = input("Enter a number. Type 'x' to quit: ")
##    if user_input.lower() == 'x': break
##    numbers_list.append(float(user_input))
##    #numbers_list.append(user input)
##    print(numbers_list)
##
##print("Loop has ended...")
##total = 0
##for number in numbers_list:
##    total += number # Shorthand for total = total + number
##
##print("Total = " + str(total))
##average = total /len(numbers_list)
##print("Average = " + str(average))
##
#################################
##Hints for assignment
##
##Comments (Name, date, what the program does)
##
##
## Use this function in your program
##It prints all of the items in your stack
def print_stack(instack):
    out_string = "[bottom]"
    for item in instack:
        out_string += " | " + item + " "

    out_string += " <- [Top]"
    return out_string
##
##
## Write your main program here...
##
## Use the append keyword to push items onto the stack.
##
## Short example for print_stack function
words = ["baseball", "stadium", "hot dogs", "beer", "bat", "umpire", "beer"]

print(print_stack(words))
