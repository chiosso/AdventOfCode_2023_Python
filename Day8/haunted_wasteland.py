## CONSTRUCT THE NETWORK AND DIRECTIONS ##

input = open('Day8/input.txt', 'r').readlines()
nodes = {}
for i in range(2,len(input)):
    node = input[i].split()[0]
    left = input[i].split('(')[1].split(',')[0]
    right = input[i].split('(')[1].split(',')[1].strip(' )\n')
    nodes[node] = (left, right)

directions = []
for c in input[0]:
    if c == 'L':
        directions.append(0)
    elif c == 'R':
        directions.append(1)


## TRAVERSE THE NETWORK ##

steps_taken = 0
current_node = 'AAA'
d = 0
while current_node != 'ZZZ':
    current_node = nodes[current_node][directions[d]]
    steps_taken = steps_taken + 1
    d = d + 1
    if d == len(directions):
        d = 0
    print('At node ' + current_node + ' after taking ' + str(steps_taken) + ' steps')
