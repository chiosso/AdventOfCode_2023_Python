
ROUNDED_ROCK = 'O'
CUBED_ROCK = '#'
EMPTY_SPACE = '.'
NUM_CYCLES = 999

## PROCESS INPUT ##

platform = open('input.txt', 'r').readlines()
for i in range(len(platform)):
    platform[i] = platform[i].rstrip()
platform_width = len(platform) # assumes square

## OBJECT MODEL ##

class Rock:
    def __init__(self, pos, type):
        self.pos = pos
        self.type = type

    def moveTo(self, pos):
        self.pos = pos


## INDEX THE ROCKS FOR NORTH ROLLING ##

rocks = []
for i in range(platform_width):
    rocks.append([])

for y in range(platform_width):
    for x in range(platform_width):
        if platform[y][x] != EMPTY_SPACE:
            rocks[x].append(Rock(y,platform[y][x]))


## ROLL THE ROCKS ##

def roll(rocks):
    for line in rocks:
        for rock_index in range(len(line)):
            if rock_index == 0:
                if line[rock_index].type == ROUNDED_ROCK:
                    line[rock_index].moveTo(0)
            else:
                if line[rock_index].type == ROUNDED_ROCK:
                    line[rock_index].moveTo(line[rock_index-1].pos+1)


## ROTATE PLATFORM CLOCKWISE ##

def rotateClockwise(rocks):
    rotated_rocks = []
    for i in range(platform_width):
        rotated_rocks.append([])

    for line_index in range(platform_width):
        for rock in rocks[line_index]:
            rotated_rocks[platform_width-1-rock.pos].append(rock)
            rock.moveTo(line_index)

    return rotated_rocks

## EXAMINE THE ROCKS ##

def rocksToString(rocks):
    s = [EMPTY_SPACE]*platform_width*platform_width
    for line_index in range(platform_width):
        for rock in rocks[line_index]:
            s[platform_width*line_index+rock.pos] = rock.type
    return ''.join(s)

def calculateTotalLoad(rocks):
    total_load = 0
    for line in rocks:
        for rock in line:
            if rock.type == ROUNDED_ROCK:
                total_load += platform_width - rock.pos
    return total_load

## RUN THE CYCLE ##

rock_strings = []

for cycle in range(NUM_CYCLES):
    for rotation in range(4):
        roll(rocks)
        rocks = rotateClockwise(rocks)
    rock_string = rocksToString(rocks)
    print('Completed cycles: ' + str(cycle + 1).zfill(3) + ' Total Load: ' + str(calculateTotalLoad(rocks)) + ' Rocks: ' + rock_string)
    if rock_string in rock_strings:
        print('Pattern found!')
        for i in range(len(rock_strings)):
            if rock_strings[i] == rock_string:
                print('This matches rock string with index ' + str(i))
        break
    else:
        rock_strings.append(rock_string)

print('End')