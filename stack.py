# Author : Levi Yates
# Date   : 2022-10-24
# This program will either pop, or push an item on to a stack depending on user input.

def print_stack(instack):
    out_string = "[bottom]"
    for item in instack:
        out_string += " | " + item + " "

    out_string += " <- [Top]"
    return out_string

thestack = []

print("Type 'u' for pUsh, 'o' for pOp, 'x' to eXit.")


for i in range(1, 100000000000000):

    theOnlyQuestion = input("u, o, or x: ")
    
    if theOnlyQuestion.lower() == "u":
        pushInput = input("Item to push on to the stack: ")
        thestack.append(str(pushInput))
        print(print_stack(thestack))

    elif theOnlyQuestion.lower() == "o" and thestack :
        popInput = input("Item popped off the stack: ")
        thestack.remove(str(popInput)) # Had problems using .pop, so I substituted for .remove.
        print(print_stack(thestack))
        
    elif theOnlyQuestion.lower() == "x": break

    else:
        print("Stack is Empty")
