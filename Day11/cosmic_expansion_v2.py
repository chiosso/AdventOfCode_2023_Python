## PROCESS INPUT ##

universe = open('Day11/input.txt', 'r').readlines()
for i in range(len(universe)):
    universe[i] = universe[i].rstrip()

expansion_coefficient = 1000000

## CALCULATE UNIVERSE EXPANSION ##

# Expand rows
i = 0
universe_width = len(universe[0])
rows_to_expand = []
while True:
    if i == len(universe):
        break
    if len(set(universe[i])) == 1 and universe[i][0] == '.':
        rows_to_expand.append(i)
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


## INDEX GALAXIES ##

galaxies = {}
id = 1
for row in range(len(universe)):
    for col in range(len(universe[0])):
        if universe[row][col] == '#':
            galaxies[id] = (row,col)
            id = id + 1


## MEASURE DISTANCES ##

def distanceBetweenGalaxies(galaxies, rows_to_expand, columns_to_expand, g1, g2):
    distance = abs(galaxies[g1][0] - galaxies[g2][0]) + abs(galaxies[g1][1] - galaxies[g2][1])
    for row_num in rows_to_expand:
        if row_num > min(galaxies[g1][0],galaxies[g2][0]) and row_num < max(galaxies[g1][0],galaxies[g2][0]):
            distance = distance + expansion_coefficient - 1
    for col_num in columns_to_expand:
        if col_num > min(galaxies[g1][1],galaxies[g2][1]) and col_num < max(galaxies[g1][1],galaxies[g2][1]):
            distance = distance + expansion_coefficient - 1
    return distance


galaxy_pairs = {}
for g1 in range(1, len(galaxies.keys()) + 1):
    for g2 in range(g1+1,len(galaxies.keys()) + 1):
        galaxy_pairs[g1,g2] = distanceBetweenGalaxies(galaxies,rows_to_expand,columns_to_expand,g1,g2)

print('Sum of distances = ' + str(sum(galaxy_pairs.values())))