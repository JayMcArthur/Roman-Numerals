import os
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

#
# This was turned in after the required time and doesn't count for the interview. Just made it because i wanted to make my attempt better
# However after relooking at the requirements I saw you wanted a way to convert both ways
# Dont know how I missed it the first time. It would put my time up to 2.5 Hrs
#

# Allows for any size of deciaml number by getting rid of hard code
def getConversion(items):
    tens = 1
    state = -1
    conversions = []

    for i in range(len(items)):
        if state == -1:
            conversions.append([tens * 1, items[i]])
        elif state == 0:
            conversions.append([tens * 4, items[i-1] + items[i]])
            conversions.append([tens * 5, items[i]])
        elif state == 1:
            conversions.append([tens * 9, items[i-2] + items[i]])
            tens *= 10
            conversions.append([tens * 1, items[i]])
        state = (state + 1) % 2

    #print(conversions)
    return conversions[::-1]

CONVERSION = getConversion(['I', 'V', 'X', 'L', 'C', 'D', 'M'])

# Does the conversion
def DecToRom(decNum):
    i = 0
    romNum = ''
    for [value, str] in CONVERSION:
        while decNum >= value:
            decNum -= value
            romNum += str
    return romNum

# Mainloop
while True:
    decNum = input("Decimal Number: ")
    if decNum == 'q':
        break
    try:
        romNum = DecToRom(int(decNum))
        print(decNum + " is " + romNum)
    except:
        print("Please input a valid Decimal Number")
    clear()
    print("\nEnter q to quit or another")