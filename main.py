import xlwt 
from xlwt import Workbook 

# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Magic Numbers') 

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

information = [0,0,0,0,0,0,0,0]

def stepUntilGoalReached(numberToStep):
    step = 0
    while numberToStep != '6174':
        numberToStep = takeAStep(numberToStep)
        step += 1
    
    print(f"Your magicNumber {magicNumber} took {step} steps to reach 6174.")
    sheet1.write(step, information[step], f"{magicNumber}") 

    information[step] += 1

    return numberToStep

while magicNumber <= 9999:
    magicNumber = 1000 + cycles 

    if isAMagicNumber(magicNumber):
        stepUntilGoalReached(str(magicNumber))

    cycles += 1 

print(information)

# Saves the workbook as a file
wb.save('xlwt example.xls') 
