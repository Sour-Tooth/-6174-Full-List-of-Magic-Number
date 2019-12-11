cycles = 0

magicNumber = 1000 + cycles

def isAMagicNumber(number):

    if len(number) == len(set(number)):
        return True
    else:
        return False
 
myMagicNumber = getMagicNumber()
print(myMagicNumber)

