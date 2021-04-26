import os, collections 
from itertools import groupby

#
# THIS USES PYTHON 3.6+
#

# Dict of all require conversions
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
def RomToDec(inStr):
    decNum = 0
    inStr = inStr.upper()
    inStr = list(''.join(group) for key, group in groupby(inStr))
    if not(all(Check(x) for x in inStr)): return None # Incorrect letters and amount
    
    pos = 0
    while pos < len(inStr):
        if not(pos + 1 == len(inStr)) and KEYS.index(inStr[pos][0]) < KEYS.index(inStr[pos + 1][0]): # Should Sub?
            diff = KEYS.index(inStr[pos][0]) - KEYS.index(inStr[pos + 1][0]) # Only -1 to -2 pos
            if (-3 < diff < 0) and len(inStr[pos]) == 1 and (pos + 2 == len(inStr) or KEYS.index(inStr[pos + 1][0]) >= KEYS.index(inStr[pos + 2][0])): # sub is only 1 long and there is not double sub
                decNum += CONVERSIONS[inStr[pos + 1][0]] * len(inStr[pos + 1]) - CONVERSIONS[inStr[pos][0]]
                pos += 2
            else: return None
        else:
            decNum += CONVERSIONS[inStr[pos][0]] * len(inStr[pos])
            pos += 1
    return decNum

# Mainloop
while True:
    romNum = input("Roman Numeral: ")
    if romNum == 'q':
        break
    decNum = RomToDec(romNum)
    if decNum is not None:
        print(romNum + " is " + str(decNum))
    else:
        print("Please input a valid Roman Numeral")
    print("\nEnter q to quit or a Roman Numeral")