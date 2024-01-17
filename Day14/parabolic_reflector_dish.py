
ROUNDED_ROCK = 'O'
CUBED_ROCK = '#'
EMPTY_SPACE = '.'

## PROCESS INPUT ##

platform = open('input.txt', 'r').readlines()
for i in range(len(platform)):
    platform[i] = platform[i].rstrip()


## OBJECT MODEL ##

class Rock:
    def __init__(self, pos, type):
        self.pos = pos
        self.type = type

    def moveTo(self, pos):
        self.pos = pos


## INDEX THE ROCKS FOR NORTH ROLLING ##

rocks = []
for i in range(len(platform[0])):
    rocks.append([])

for y in range(len(platform)):
    for x in range(len(platform[y])):
        if platform[y][x] != EMPTY_SPACE:
            rocks[x].append(Rock(y,platform[y][x]))


## ROLL THE ROCKS ##

for line in rocks:
    for rock_index in range(len(line)):
        if rock_index == 0:
            if line[rock_index].type == ROUNDED_ROCK:
                line[rock_index].moveTo(0)
        else:
            if line[rock_index].type == ROUNDED_ROCK:
                line[rock_index].moveTo(line[rock_index-1].pos+1)


## CALCULATE LOAD ##

total_load = 0

for line in rocks:
    for rock in line:
        if rock.type == ROUNDED_ROCK:
            total_load += len(platform) - rock.pos

print('Total load = ' + str(total_load))