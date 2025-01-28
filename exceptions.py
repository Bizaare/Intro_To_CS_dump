# Author : Levi Yates
# Date   : 2022-11-14
# This program demonstrates the use of exception handling

# Have the user enter two numbers.
# Divide the first number by the second number & print the results

print("=======================================")
print("This program divides two whole numbers.")
print("Enter 'x' to exit the program.")

while True:
    try:
        input1 = input("Input the first number: ").lower()
        if input1 == 'x': break
        input2 = input("Input the second number: ").lower()
        if input2 == 'x': break

        
        num1 = int(input1)
        num2 = int(input2)

        print("You entered " + str(num1) + " and " + str(num2))

       
        result = num1 / num2
        print("Result = " + str(result))

    except ValueError as ex:
        print("Error: No letters or special characters allowed.")

    except ZeroDivisionError as ax:
        print("Error: No zeros can be used as the second number.")

    except KeyboardInterrupt as qx:
        print("You tried to stop the program.")
        print("Enter 'x' to exit the program.")

    print()
    print("Do it all over again...")
    print()

print("Program has ended.")
