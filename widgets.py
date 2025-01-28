# Author : Levi Yates
# Date   : 2022-08-29
# This program computes the total sales of widgets.

mnSalesTaxRate = 0.06875 # 6 7/8 %
widgetPrice = 10.99 #Price of our widget

quantity =  int(input("How many widgets would you like to purchase? "))

subTotal = quantity * widgetPrice
print("Quantity = " + str(quantity) + " at $" +str(widgetPrice)
      + " each = $" + str(subTotal) + " SubTotal")

salesTax = subTotal * mnSalesTaxRate
print("MN sales tax = $" + str(salesTax))

totalSale = subTotal + salesTax
print("Total Cost: $" + str(totalSale))

print()
print("Reformatted nicely...")
print("Quantity = " + str(quantity) + " at $" + str(widgetPrice)
      + " each = $" + format(subTotal, '0,.2f') + " SubTotal")

print()
salesTax = subTotal * mnSalesTaxRate
print("MN sales tax = $" + format(salesTax, '0,.2f'))

totalSale = subTotal + salesTax
print("Total Sale = $" + format(totalSale, '0,.2f'))

print()
print("SubTotal   = $ " + format(subTotal,  '10,.2f'))
print("Sales Tax  = $ " + format(salesTax,  '10,.2f'))
print("Total Sale = $ " + format(totalSale, '10,.2f'))

# End of program.
