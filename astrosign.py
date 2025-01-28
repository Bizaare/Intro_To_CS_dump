# Author : Levi Yates
# Date   : 2022-09-13
# This program will tell you your astrological sign based on birthday.

print("Learn what your atrological sign is based on your birthday.")

PASS = True


 ## Months input
month = int(input("What is your birth month? (1-12) "))

if month > 12:
    print("Sorry, you must enter a working integer (months.)")
    PASS = False
if month < 1:
    print("Sorry, you must enter a working integer (months.)")
    PASS = False


 ## Days input   
if PASS:    
    day = int(input("What is your birth day? (1-31) "))

    if day > 31:
        print("Sorry, you must enter a working integer (days.)")
        PASS = False
    if day < 1:
        print("Sorry, you must enter a working integer (days.)")
        PASS = False
    if month == 2 and day > 29:
        print("Sorry, you must enter a working integer (days.)")
        PASS = False
    if month == 9 and day > 30:
        print("Sorry, you must enter a working integer (days.)")
        PASS = False
    if month == 11 and day > 30:
        print("Sorry, you must enter a working integer (days.)")
        PASS = False


if PASS:
    birthday = input(str(month) + "-" + str(day) + " Is your selected birthday. is this correct? ")
    if birthday != "y":
        print("Please restart to fix your birthday.")
        PASS = False
    
 ## astrological output        
if PASS:
    ## Aquarius ##
    if month == 1 and day >= 21:
        print("Your astrological sign is Aquarius")
    if month == 2 and day <= 19:
        print("Your astrological sign is Aquarius")
    ## Pisces ##
    if month == 2 and day >= 20:
        print("Your astrological sign is Pisces")
    if month == 3 and day <= 20:
        print("Your astrological sign is Pisces")
    ## Aries ##
    if month == 3 and day >= 21:
        print("Your astrological sign is Aries")
    if month == 4 and day <= 20:
        print("Your astrological sign is Aries")
    ## Taurus ##
    if month == 4 and day >= 21:
        print("Your astrological sign is Taurus")
    if month == 5 and day <= 20:
        print("Your astrological sign is Taurus")
    ## Gemini ##
    if month == 5 and day >= 21:
        print("Your astrological sign is Gemini")
    if month == 6 and day <= 21:
        print("Your astrological sign is Gemini")
    ## Cancer ##
    if month == 6 and day >= 22:
        print("Your astrological sign is Cancer")
    if month == 7 and day <= 22:
        print("Your astrological sign is Cancer")
    ## Leo ##
    if month == 7 and day >= 23:
        print("Your astrological sign is Leo")
    if month == 8 and day <= 23:
        print("Your astrological sign is Leo")
    ## Virgo ##
    if month == 8 and day >= 24:
        print("Your astrological sign is Virgo")
    if month == 9 and day <= 22:
        print("Your astrological sign is Virgo")
    ## Libra ##
    if month == 9 and day >= 23:
        print("Your astrological sign is Libra")
    if month == 10 and day <= 22:
        print("Your astrological sign is Libra")
    ## Scorpio ##
    if month == 10 and day >= 23:
        print("Your astrological sign is Scorpio")
    if month == 11 and day <= 22:
        print("Your astrological sign is Scorpio")
    ## Sagittarius ##
    if month == 11 and day >= 23:
        print("Your astrological sign is Sagittarius")
    if month == 12 and day <= 21:
        print("Your astrological sign is Sagittarius")
    ## Capricorn ##
    if month == 12 and day >= 22:
        print("Your astrological sign is Capricorn")
    if month == 1 and day <= 20:
        print("Your astrological sign is Capricorn")

# End of Program
