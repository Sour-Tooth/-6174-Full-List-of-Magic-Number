cycles = 0
magicNumber = 1234

while magicNumber <= 9999:
    magicNumber = 1000 + cycles

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

    if isAMagicNumber(magicNumber):
        print(magicNumber)

    cycles += 1 
