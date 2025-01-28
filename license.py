# Author : Levi Yates
# Date   : 2022-09-12
# This program utilizes the if/else and boolean logic

# Boolean -- True / False 1 / 0 On / Off and or not

a = True
b = True

# a  b  or and
# F  F  F  F
# F  T  T  F
# T  F  T  F
# T  T  T  T

##if a and b:
##    print("And evaluates to True")
##else:
##    print("And evaluates to False")
##
##    
##if a or b:
##    print("Or evaluates to True")
##else:
##    print("Or evaluates to False")
##
##
##if a and not b:
##    print("The statement evaluated to True")
##else:
##    print("The statement evaluated to False")



##x = 3
##y = 6
##z = 17
##
##if z != x * y:
##    print("Evaluates to True")
##    print("This is part of the true block.")
##    print("This is also part of the true block.")
##else:
##    print("Evaluates to False")
##    print("This is part of the false block.")
##
##print("This is outside of the comparison")

# The following percentage distribution guarantees the following grade:
# A: 93%+  A-:90%+  B+:87%+  B:83%+  B-:80%+  C+:77%+  C: 73%+  C-:70%+  D+:67%  D:63%+  D-:60%+  F:<60%

# > < >= <= == != or and not


##score = int(input("Enter a test score: "))
##print("You entered a score of " + str(score) + "%")
##
##if score >= 93:
##    print("A")
##
##if score < 93 and score >= 90:
##    print("A-")
##
##if score < 90 and score >= 87:
##    print("B+")
##
##if score < 87 and score >= 83:
##    print("B")
##
##if score < 83 and score >= 80:
##    print("B-")
##
##if score < 80 and score >= 77:
##    print("C+")
##
##if score < 77 and score >= 73:
##    print("C")
##
##if score < 73 and score >= 70:
##    print("C-")
##
##if score < 70 and score >= 67:
##    print("D+")
##
##if score < 67 and score >= 63:
##    print("D")
##
##if score < 63 and score >= 60:
##    print("D-")
##
##if score < 60:
##    print("F")

# The following percentage distribution guarantees the following grade:
# A: 93%+  A-:90%+  B+:87%+  B:83%+  B-:80%+  C+:77%+  C: 73%+  C-:70%+  D+:67%

##score = float(input("Enter a test score: "))
##print("You entered a score of " + str(score) + "%")
##
##if score >= 93:
##    print("A")
##elif score >= 90:
##    print("A-")
##elif score >= 87:
##    print("B+")
##elif score >= 83:
##    print("B")
##elif score >= 80:
##    print("B-")
##elif score >= 77:
##    print("C+")
##elif score >= 73:
##    print("C")
##elif score >= 70:
##    print("C-")
##elif score >= 67:
##    print("D+")
##elif score >= 63:
##    print("D")
##elif score >= 60:
##    print("D-")
##elif score >= 0:
##    print("F")
    

# This program determines if a person is qualifiede to have a driver's license.
# Must be 16 years old or above
# Must have driver's education if younger than 17.5 years old
# Must have permit at least 6 months less than 18
# Must have learner's permit at least 3 months if 18 or older
# Must have complete supervised driving
# Must pass behind the wheel exam
# Must pass vision screening

OK = True # sentinel value

age = float(input("What is your age in years? "))

if age < 16:
            print("Sorry, you must be at least 16 years of age.")
            OK = False

if OK and age < 17.5:
            answer = input("Have you had driver's training yet (y/n)? ").lower()[:1]
            if answer != "y":
                print("Sorry, you must have driver's education training first.")
                OK = False
            else:
                print("answer was yes")
                           
if OK:
    months = int(input("How many months have you had your learner's permit? "))
    if not((age < 18 and months >= 6) or (age >= 18 and months >= 3)):
        print("Sorry, you must have had your learner's permit for at least")
        print("6 months if less than 18 years of age, or at least 3 months if 18 years of age or older.")
        OK = False

if OK and age < 18:
    answer = input("Do you have supervised hours log with at least 50 hours of time (y/n)? ").lower()[:1]
    if answer != "y":
        print("Sorry, you must have completed a log of at least 50 hours.")
        OK = False

if OK:
    answer = input("Did you pass your bheind the wheel exam (y/n)? ").lower()[:1]
    if answer != "y":
        print("Sorry, you must pass your behind the wheel exam.")
        OK = False

if OK:
    answer = input("Did you pass your vision screening (y/n)? ").lower()[:1]
    if answer != "y":
        print("Sorry, please get your vision checled by an eye car professional.")
        OK = False

if OK:
    print("Congratulations, you may be issued a driver's license.")
else:
    print("Sorry,. you do not qualify for a driver's license.")
                      










# End of program.
