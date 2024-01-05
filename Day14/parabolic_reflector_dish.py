from Day14 import cursor

ROUNDED_ROCK = 'O'
EMPTY_SPACE = '.'

## PROCESS INPUT ##

platform = open('Day14/test_input.txt', 'r').readlines()
for i in range(len(platform)):
    platform[i] = platform[i].rstrip()



## INDEX THE ROUNDED ROCKS FOR NORTH ROLLING ##

rounded_rocks = []

for pos_y in range(len(platform)):
    for pos_x in range(len(platform[pos_y])):
        if platform[pos_y][pos_x] == ROUNDED_ROCK:
            rounded_rocks.append((pos_y,pos_x))


## ROLL THE ROCKS ##

for rounded_rock in rounded_rocks:
    if rounded_rock[0] > 0: # ignore top row
        y = rounded_rock[0]
