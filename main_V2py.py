import os, collections 
from itertools import groupby
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

#
# THIS USES PYTHON 3.6+
#

# Map of all require conversions
CONVERSIONS = collections.OrderedDict((
    ('I', 1),
    ('V', 5),
    ('X', 10),
    ('L', 50),
    ('C', 100),
    ('D', 500),
    ('M', 1000)
))

KEYS = list(CONVERSIONS.keys())


def Check(a):
    for i in KEYS:
        if i == a[0]: 
            if len(a) <= ((KEYS.index(i) + 1) % 2) * 2 + 1:
                return True
    return False

# Converter
def RomToDec(str):
    decNum = 0
    str = str.upper()
    str = list(''.join(group) for key, group in groupby(str))
    if not(all(Check(x) for x in str)): return None # Incorrect letters and amount
    
    pos = 0
    while pos < len(str):
        if not(pos + 1 == len(str)) and KEYS.index(str[pos][0]) < KEYS.index(str[pos + 1][0]): # Should Sub?
            diff = KEYS.index(str[pos][0]) - KEYS.index(str[pos + 1][0])
            if -3 < diff and diff < 0 and (len(str) - 2 == pos or KEYS.index(str[pos+1][0]) >= KEYS.index(str[pos+2][0])): # is it only 2 less and there isnt double sub
                decNum += CONVERSIONS[str[pos + 1][0]] * len(str[pos + 1]) - CONVERSIONS[str[pos][0]]
                pos += 2
            else: return None
        else:
            decNum += CONVERSIONS[str[pos][0]] * len(str[-1])
            pos += 1
    return decNum

# Mainloop
while True:
    clear()
    romNum = input("\nRoman Numeral: ")
    decNum = RomToDec(romNum)
    if decNum != None:
        print(romNum + " is " + str(decNum))
    else:
        print("Please input a valid Roman Numeral")
    again = input("\nAgain : (y/n) ")
    if again == "y" or again == '1':
        pass
    else:
        break