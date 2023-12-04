class Card:
    def __init__(self, name, myNumbers, winningNumbers):
        self.name = name
        self.instances = 1
        self.numMatches = len(myNumbers.intersection(winningNumbers))

    def addInstances(self, n):
        self.instances = self.instances+n

    def __str__(self):
        return self.name + ': NumMatches ' + str(self.numMatches) + ' Instances ' + str(self.instances)



lines = open('C:\\Users\\tim\\dev\\AdventOfCode_2023_Python\\Day4\\input.txt','r').readlines()
cards = []

for line in lines:
    name = line.split(':')[0]
    numbers = line.split(':')[1].split('|')
    cards.append(Card(name, set(numbers[0].split()), set(numbers[1].split())))

for i in range(len(cards)):
    for p in range(1,cards[i].numMatches+1):
        cards[i+p].addInstances(cards[i].instances)

for card in cards:
    print(card)

totalNumberOfCards = 0
for card in cards:
    totalNumberOfCards = totalNumberOfCards+card.instances

print('Total number of cards: ' + str(totalNumberOfCards))
