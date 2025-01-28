# Author : Levi Yates
# Date   : 2022-10-17
# Exploration of Regular Expressions

# Note: put parenthesis () around the entire regex pattern
# to create an entire match.

import re # Load in the regular expression library.

myString = "Vat #1 Temperature 94.2F. " \
        "Vat #2 Temperature 99.5F. " \
        "Vat #3 Temperature 93.2. " \
        "Vat #4 Temperature 108.9F. " \
        "This freezer is really cold as it is -12.5F inside. " \
        " My other freezer is -8.4F." \

print(myString)

# This is our regular expression pattern.
# It finds a temperature in a string.
# Temperature can be from -999.9F to 999.9F

pattern = '(-?\d{1,3}\.\dF)'

matches = re.findall(pattern, myString)

print("matches = " + str(matches))
print()

for match in matches:
    print("Temperature found = " + str(match))

print()

print("The temperature for Vat #3 is " + str(matches[2]))
print()

townString = """These are local towns in the Ridgewater College area and their ZIP codes. Ridgewater College in Hutchinson 55350-3100. Ridgewater College in Willmar 56201-2098. Hutchinson 55350. Willmar 56201. Litchfield 55355. Lake Lillian 56253. Cosmos 56228"""

print(townString)

pattern = '(\d{5}(-\d{4})?)'

matches = re.findall(pattern, townString)

print("matches = " + str(matches))
print()

for match in matches:
    print("ZIP code found = " + str(match[0]))

print()

sentence = """Ridgewater College is in MN.
The sun is shinint in AZ. AL is hot and humid.
FL just had a hurricane. This is WX and is not a valid state name.
I haave visited PR and it was nice."""

pattern = '((AL)|(AK)|(AS)|(AZ)|(AR)|(CA)|(CO)|(CT)|(DE)|(DC)|(FM)|(FL)|(GA)|(GU)|(HI)|(ID)|(IL)|(IN)|(IA)|(KS)|(KY)|(LA)|(ME)|(MH)|(MD)|(MA)|(MI)|(MN)|(MS)|(MO)|(MT)|(NE)|(NV)|(NH)|(NJ)|(NM)|(NY)|(NC)|(ND)|(MP)|(OH)|(OK)|(OR)|(PW)|(PA)|(PR)|(RI)|(SC)|(SD)|(TN)|(TX)|(UT)|(VT)|(VI)|(VA)|(WA)|(WV)|(WI)|(WY))'

matches = re.findall(pattern, sentence)

#print("matches = " + str(matches))
#print()

for match in matches:
    print("State abbreviation found = " + str(match[0]))
print()
