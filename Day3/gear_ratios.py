## LOAD INPUT ##

input_file_path = 'C:\\Users\\tim\\python\\AdventOfCode_2023\\Day3\\input.txt'
input_file = open(input_file_path, 'r')
schematic = input_file.readlines()

# REMOVE NEWLINES ##
for i in range(len(schematic)):
    schematic[i] = schematic[i].rstrip()

matrixRightmostIndex = len(schematic[0])-1

## OBJECTS ##

class PartNumberCandidate:
    def __init__(self, value, lineNumber, firstCharIndex):
        self.value = value
        self.lineNumber = lineNumber
        self.firstCharIndex = firstCharIndex

    def leftBound(self):
        if self.firstCharIndex == 0:
            return 0
        else:
            return self.firstCharIndex-1

    def rightBound(self):
        rightBound = self.firstCharIndex + len(str(self.value))
        if rightBound > matrixRightmostIndex:
            return matrixRightmostIndex
        else:
            return rightBound

    def __str__(self):
        return 'PartNumberCandidate: Value ' + str(self.value) + ' LineNum ' + str(self.lineNumber) + ' LeftBound ' + str(self.leftBound()) + ' RightBound ' + str(self.rightBound())
        

## EXTRACT ALL THE PART NUMBER CANDIDATES ##

partNumberCandidates = []
processingANumber = False

for y in range(len(schematic)):
    c = schematic[y]
    for x in range(len(c)):
        if processingANumber:
            if c[x].isdigit(): # Middle of a number
                numberString = numberString + c[x]
            if c[x].isdigit() == False or x == matrixRightmostIndex: # End of a number
                partNumberCandidates.append(PartNumberCandidate(numberString,y,firstCharIndex))
                processingANumber = False
                numberString=''
        elif c[x].isdigit(): # Start of a number
            processingANumber = True
            numberString = c[x]
            firstCharIndex = x

## CHECK IF IT'S A VALID PART NUMBER ##

def isSymbol(char):
    return char != '.' and char.isdigit() == False

def doesNumberHaveAdjacentSymbol(pnc):
    if isSymbol(schematic[pnc.lineNumber][pnc.leftBound()]):
        return True
    if isSymbol(schematic[pnc.lineNumber][pnc.rightBound()]):
        return True
    if pnc.lineNumber != 0:
        for x in range(pnc.leftBound(), pnc.rightBound()+1):
            if (isSymbol(schematic[pnc.lineNumber-1][x])):
                return True
    if pnc.lineNumber != len(schematic)-1:
        for x in range(pnc.leftBound(), pnc.rightBound()+1):
            if (isSymbol(schematic[pnc.lineNumber+1][x])):
                return True
    return False

## SUM UP ALL THE PART NUMBERS ##

partNumbersSum = 0
for p in partNumberCandidates:
    validPN = doesNumberHaveAdjacentSymbol(p)
    print(str(p) + ' AdjSymbol ' + str(validPN))
    if validPN:
        partNumbersSum = partNumbersSum + int(p.value)

print('Total sum: ' + str(partNumbersSum))


## PART 2 ##

gears = {}
goodGearKeys = []

def putGear(y, x, value):
    gearKey = str(y) + '|' + str(x)
    if gearKey in gears:
        gears[gearKey] = gears[gearKey] * value
        goodGearKeys.append(gearKey)
    else:
        gears[gearKey] = value

for pnc in partNumberCandidates:
    if schematic[pnc.lineNumber][pnc.leftBound()] == '*':
        putGear(pnc.lineNumber, pnc.leftBound(), int(pnc.value))
    if schematic[pnc.lineNumber][pnc.rightBound()] == '*':
        putGear(pnc.lineNumber, pnc.rightBound(), int(pnc.value))
    if pnc.lineNumber != 0:
        for x in range(pnc.leftBound(), pnc.rightBound()+1):
            if schematic[pnc.lineNumber-1][x] == '*':
                putGear(pnc.lineNumber-1, x, int(pnc.value))
    if pnc.lineNumber != len(schematic)-1:
        for x in range(pnc.leftBound(), pnc.rightBound()+1):
            if schematic[pnc.lineNumber+1][x] == '*':
                putGear(pnc.lineNumber+1, x, int(pnc.value))

print('Gears ' + str(gears))
print('Good gear keys ' + str(goodGearKeys))

sumOfGearRatios = 0
for gearKey in goodGearKeys:
    sumOfGearRatios = sumOfGearRatios + gears[gearKey]

print('Total sum: ' + str(sumOfGearRatios))
