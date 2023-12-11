from enum import Enum

## OBJECT MODEL ##

class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

class Hand:
    def __init__(self, cardsString, bid):
        self.cards = {}
        self.cardsString = cardsString
        self.bid = int(bid)
        for c in cardsString:
            if c in self.cards:
                self.cards[c] = self.cards[c]+1
            else:
                self.cards[c] = 1

    def getHandType(self):
        if len(self.cards.keys()) == 1:
            return HandType.FIVE_OF_A_KIND
        if 4 in self.cards.values():
            return HandType.FOUR_OF_A_KIND
        if 3 in self.cards.values() and 2 in self.cards.values():
            return HandType.FULL_HOUSE
        if 3 in self.cards.values():
            return HandType.THREE_OF_A_KIND
        if len(self.cards.keys()) == 3 and 2 in self.cards.values():
            return HandType.TWO_PAIR
        if 2 in self.cards.values():
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD

    def __str__(self):
        return 'Hand <' + self.cardsString + '>: ' + str(self.getHandType())

def generateSortStringForHand(hand):
    return hand.cardsString.replace('A','E').replace('K','D').replace('Q','C').replace('J','B').replace('T','A')

def testSort(s):
    return s.replace('l','v')

## READ INPUT ##

lines = open('C:\\Users\\tim\\dev\\AdventOfCode_2023_Python\\Day7\\input.txt', 'r').readlines()
hands = {}
for line in lines:
    line = line.split()
    hand = Hand(line[0], line[1])
    if (hand.getHandType() in hands.keys()):
        hands[hand.getHandType()].append(hand)
    else:
        hands[hand.getHandType()] = [hand]


## PROCESS HANDS ##

for group in hands.values():
    group.sort(key=generateSortStringForHand)

total_winnings = 0
rank = 1
for type in HandType:
    if type in hands.keys():
        for hand in hands[type]:
            total_winnings = total_winnings + hand.bid * rank
            print(str(hand) + ' rank ' + str(rank))
            rank = rank + 1

print('Total winnings: ' + str(total_winnings))