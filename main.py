import random

def getMagicNumber():
    numberFound = False
    while numberFound == False:
        randomNumber = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9) ]

        if len(randomNumber) == len(set(randomNumber)):
            numberFound = True

            magicNumber = ''
            for number in randomNumber:
                magicNumber += str(number)
            
            return magicNumber
    
myMagicNumber = getMagicNumber()
print(myMagicNumber)
