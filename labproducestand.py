# Author : Levi Yates
# Date  : 2022-10-31
# This program calculates price of produce sold at a produce stand.

#Hints
#print("Split input example.")
##line = input("Quantity and Item: ").lower()
##x = line.split(" ")
##print(x)
##quant = int(x[0])
#item = x[1]
#print("Quantity = " + str(quant))
#print("Item = " + item)

##print()
##price = 0.90
##print("$" + format(price, '0.2f'))
##
##print()
##
##
##print()

# When creating your dictionary, the item(keys) are strings.
# The prices (values) are just floating point numbers (not a string).

# You need a loop that keeps going until quantity entered is a 0.

# use a variable to hold your total.
totalprice = 0
foodPrices = {"carrot":0.05, "tomato":0.95, "cucumber":0.20, "potato":0.45,
              "apple":0.45, "lettuce":1.10, "onion":0.55}
for i in range(1, 100000000000000):
    print("Type the quantity and item name. '0' to exit.")
    line = input("Quantity and Item: ").lower()
    x = line.split(" ")
    quant = int(x[0])
    if quant > 0:
        item = x[1]
        if item in foodPrices.keys():
            totalprice += foodPrices.get(item) * quant
            price = foodPrices.get(item)
            print(str(quant) + " " + str(item) + " @ $" + str(price) + " each = " + str(price*quant))
            
        elif item not in foodPrices.keys():
            print("Item not found")

    elif quant == 0:
        print("======================")
        print("$" + format(totalprice, '0.2f'))
        break
