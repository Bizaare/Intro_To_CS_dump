# Author : Levi Yates
# Date   : 2022-11-19
# This program reads a file containing elements from the periodic table, and reads for errors

try:
    with open("elements.txt", "r") as file:
        lines = []
        for i, line in enumerate(file, 1):
            if i > 10: break                  
            lines.append(line.strip())
            print(i, line.strip())         
except FileNotFoundError as ex:
    print("Error: File elements.txt not found.")
print("End of program.")
