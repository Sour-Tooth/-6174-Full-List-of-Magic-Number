import random

def createAMagicNumber():
    numberFound = False
    while numberFound == False:
        randomNumber = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9) ]

        if len(randomNumber) == len(set(randomNumber)):
            numberFound = True

            magicNumber = ''
            for number in randomNumber:
                magicNumber += str(number)

            print(f"Your magicNumber is: {magicNumber}")
            return magicNumber
    
def takeAStep(numberToStep):
    lowToHi = ''.join(sorted(numberToStep))
    print(f"Your magicNumber organized from low-high is: {lowToHi}")

    hiToLow = ''.join(sorted(numberToStep, reverse = True))
    print(f"Your magicNumber organized from high-low is: {hiToLow}")

    result = str(int(hiToLow) - int(lowToHi))
    print(f"Your magicNumber moved one step through the process is: {result}")

    return result

def stepUntilGoalReached(numberToStep):
    step = 0
    while numberToStep != '6174':
        numberToStep = takeAStep(numberToStep)
        step += 1
        print(f"Your number at step {step} is: {numberToStep}")

    return numberToStep
        
myMagicNumber = createAMagicNumber()
myMagicNumber = stepUntilGoalReached(myMagicNumber)