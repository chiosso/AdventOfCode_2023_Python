cards = open('C:\\Users\\tim\\dev\\AdventOfCode_2023_Python\\Day4\\test_input.txt','r').readlines()
totalPoints = 0

## PART 1 ##

for card in cards:
    numbers = card.split(':')[1].split('|')
    myNumbers = set(numbers[0].split())
    winningNumbers = set(numbers[1].split())
    myWinningNumbers = myNumbers.intersection(winningNumbers)
    cardPoints = 0
    if len(myWinningNumbers) > 0:
        cardPoints = 2**(len(myWinningNumbers)-1)
    #print (card.split(':')[0] + ': ' + str(myWinningNumbers) + ' points: ' + str(cardPoints))
    totalPoints = totalPoints + cardPoints
print('Part 1 total points: ' + str(totalPoints))


## PART 2 ##

class Card:
    def __init__(self, name, myNumbers, winningNumbers):
        self.name = name
        self.instances = 0
        self.points = 0
        myWinningNumbers = myNumbers.intersection(winningNumbers)
        if len(myWinningNumbers) > 0:
            self.points = 2**(len(myWinningNumbers)-1)

    def __str__(self):
        return self.name + ': Points ' + str(self.points) + ' Instances ' + str(self.instances)

for card in cards:
    name = card.split(':')[0]
    numbers = card.split(':')[1].split('|')
    print(Card(name, set(numbers[0].split()), set(numbers[1].split())))
