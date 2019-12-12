cycles = 0
magicNumber = 1234

def removeDuplicatesFromString(string):
    result = ''
    for character in string:
        if not(character in result):
            result = result + character
    
    return result

def isAMagicNumber(number):
    string = str(number)

    if len(string) == len(removeDuplicatesFromString(string)):
        return True
    else:
        return False

def takeAStep(numberToStep):
    lowToHi = ''.join(sorted(numberToStep))
    hiToLow = ''.join(sorted(numberToStep, reverse = True))
    result = str(int(hiToLow) - int(lowToHi))
    return result

def stepUntilGoalReached(numberToStep):
    step = 0
    while numberToStep != '6174':
        numberToStep = takeAStep(numberToStep)
        step += 1
    
    print(f"Your magicNumber {magicNumber} took {step} steps to reach 6174.")

    return numberToStep

while magicNumber <= 9999:
    magicNumber = 1000 + cycles 

    if isAMagicNumber(magicNumber):
        stepUntilGoalReached(str(magicNumber))

    cycles += 1 