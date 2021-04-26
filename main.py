import os, collections 
from itertools import groupby
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

#
# THIS USES PYTHON 3.6+
#

# Map of all require conversions
CONVERSIONS = collections.OrderedDict((
    ('I', [1, 3]),
    ('V', [5, 1]),
    ('X', [10, 3]),
    ('L', [50, 1]),
    ('C', [100, 3]),
    ('D', [500, 1]),
    ('M', [1000, 3])
))

# Error checking
def Check(a):
    for i in CONVERSIONS.keys():
        if i == a: return True
    return False

def SubCheck(str, i):
    if not(list(CONVERSIONS.keys()).index(str[i][0]) >= list(CONVERSIONS.keys()).index(str[i+1][0]) - 2):
        return False
    elif not(list(CONVERSIONS.keys()).index(str[i][0]) < list(CONVERSIONS.keys()).index(str[i+1][0])):
        return False
    elif not(len(str[i]) == 1):
        return False
    elif not((list(CONVERSIONS.keys()).index(str[i][0])+1) % 2):
        return False
    else:
        return True

# Converter
def RomToDec(str):
    str = list(''.join(group) for key, group in groupby(str))

    # Make sure it follows length requires
    for i in str:
        if len(i) > CONVERSIONS[i[0]][1]:
            return None

    decNum = 0
    doubleSub = 0
    for i in range(len(str) - 1):
        if SubCheck(str, i):
            decNum -= CONVERSIONS[str[i][0]][0]
            if doubleSub or doubleSub <= -1:
                return None
            else:
                doubleSub += 1
        elif list(CONVERSIONS.keys()).index(str[i][0]) >= list(CONVERSIONS.keys()).index(str[i+1][0]):
            decNum += CONVERSIONS[str[i][0]][0] * len(str[i])
            doubleSub -= 1
        else:
            return None
    decNum += CONVERSIONS[str[-1][0]][0] * len(str[-1])
    return decNum

# Mainloop
while True:
    clear()
    romNum = input("\nRoman Numeral: ")

    romNum = romNum.upper()
    if not(all(Check(x) for x in romNum)):
        print("Please input a valid Roman Numeral")
    else:
        decNum = RomToDec(romNum)
        if decNum != None:
            print(romNum + " is " + str(decNum))
        else:
            print("Please input a valid Roman Numeral")
        again = input("\nAgain : (y/n) ")
        if again == "y" or again == 1:
            pass
        else:
            break


