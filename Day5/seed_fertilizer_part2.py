from datetime import datetime

class RangeMap:
    def __init__(self, valuesTriplet):
        self.destinationRangeStart = valuesTriplet[0]
        self.sourceRangeStart = valuesTriplet[1]
        self.rangeLen = valuesTriplet[2]

    def isInRange(self, sourceValue):
        if sourceValue >= self.sourceRangeStart and sourceValue < (self.sourceRangeStart+self.rangeLen):
            return True
        else:
            return False

    def map(self, sourceValue):
        if self.isInRange(sourceValue):
            return self.destinationRangeStart + sourceValue - self.sourceRangeStart
        else:
            print('Error - tried to map for value not in range')

    def __str__(self):
        return 'RangeMap: destinationRangeStart ' + str(self.destinationRangeStart) + ' sourceRangeStart ' + str(self.sourceRangeStart) + ' rangeLen ' + str(self.rangeLen)



class AlmanacMap:
    def __init__(self, name, rangeMaps):
        self.name = name
        self.rangeMaps = rangeMaps

    def map(self, sourceValue):
        for rangeMap in self.rangeMaps:
            if rangeMap.isInRange(sourceValue):
                return rangeMap.map(sourceValue)
        return sourceValue

    def __str__(self):
        s = self.name + ' map'
        for rangeMap in self.rangeMaps:
            s = s + '\n\t' + str(rangeMap)
        return s

## READ INPUT AND GENERATE MAPS ##

lines = open('C:\\Users\\tim\\dev\\AdventOfCode_2023_Python\\Day5\\input.txt','r').readlines()

seeds = list(map(int, lines[0].split(':')[1].split()))

mapName = ''
rangeMaps = []
almanacMaps = []
for i in range(2, len(lines)):
    if lines[i].endswith('map:\n'):
        if mapName != '':
            almanacMaps.append(AlmanacMap(mapName,rangeMaps))
            rangeMaps = []
        mapName = lines[i].split()[0]
    elif len(lines[i]) > 1:
        rangeMaps.append(RangeMap(list(map(int, lines[i].split()))))
almanacMaps.append(AlmanacMap(mapName,rangeMaps))



## TRAVERSE THE MAPS ##

lowestLocationNumber = 'na'
i = 0
while i < len(seeds):
    startRange=seeds[i]
    rangeLen=seeds[i+1]
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' Processing seed range ' + str(startRange) + ' ' + str(rangeLen))
    for n in range(startRange,startRange+rangeLen):
        #print('\nSeed ' + str(n))
        for a in almanacMaps:
            n = a.map(n)
            #print(a.name + ' -> ' + str(n))
        if lowestLocationNumber == 'na':
            lowestLocationNumber = n
        elif n < lowestLocationNumber:
            lowestLocationNumber = n
    i=i+2

print('\nLowest location number: ' + str(lowestLocationNumber))
