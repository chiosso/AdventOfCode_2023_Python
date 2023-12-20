## PROCESS INPUT ##

universe = open('Day11/input.txt', 'r').readlines()
for i in range(len(universe)):
    universe[i] = universe[i].rstrip()

## EXPAND UNIVERSE ##

# Expand rows
i = 0
universe_width = len(universe[0])
while True:
    if i == len(universe):
        break
    if len(set(universe[i])) == 1 and universe[i][0] == '.':
        universe.insert(i+1,'.'*universe_width)
        i = i + 2
    else:
        i = i + 1

# Expand columns
columns = []
for i in range(universe_width):
    columns.append(set())
for row in universe:
    for i in range(universe_width):
        columns[i].add(row[i])
columns_to_expand = []
for i in range(len(columns)):
    if len(columns[i]) == 1 and '.' in columns[i]:
        columns_to_expand.append(i)
# Account for fact that each added column will push the next out one further
for i in range(len(columns_to_expand)):
    columns_to_expand[i] = columns_to_expand[i] + i
def insertDotIntoStringAtIndex(string, index):
    return string[:index] + '.' + string[index:]
for row in range(len(universe)):
    for i in columns_to_expand:
        universe[row] = insertDotIntoStringAtIndex(universe[row],i)

## INDEX GALAXIES ##

galaxies = {}
id = 1
for row in range(len(universe)):
    for col in range(len(universe[0])):
        if universe[row][col] == '#':
            galaxies[id] = (row,col)
            id = id + 1

## MEASURE DISTANCES ##

def distanceBetweenGalaxies(galaxies, g1, g2):
    return abs(galaxies[g1][0] - galaxies[g2][0]) + abs(galaxies[g1][1] - galaxies[g2][1])

galaxy_pairs = {}
for g1 in range(1, len(galaxies.keys()) + 1):
    for g2 in range(g1+1,len(galaxies.keys()) + 1):
        galaxy_pairs[g1,g2] = distanceBetweenGalaxies(galaxies,g1,g2)

print('Sum of distances = ' + str(sum(galaxy_pairs.values())))