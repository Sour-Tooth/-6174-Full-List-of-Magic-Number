import random

def getMagicNumber():
    numberFound = False

    while numberFound == False:
        magicNumber = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9) ]

        if len(magicNumber) == len(set(magicNumber)):
            return magicNumber
        else:
            numberFound = False
    
myMagicNumber = getMagicNumber()
print(myMagicNumber)
