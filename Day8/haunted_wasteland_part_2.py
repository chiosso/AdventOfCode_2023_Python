## CONSTRUCT THE NETWORK AND DIRECTIONS ##

input = open('input.txt', 'r').readlines()
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

def nodesEndingInA(node):
    if node[2] == 'A':
        return True
    return False

def doAllNodesEndInZ(nodes):
    for node in nodes:
        if node[2] != 'Z':
            return False
    return True

steps_taken = 0
current_nodes = list(filter(nodesEndingInA, list(nodes.keys())))
d = 0
while doAllNodesEndInZ(current_nodes) == False:
    for n in range(len(current_nodes)):
        current_nodes[n] = nodes[current_nodes[n]][directions[d]]
    steps_taken = steps_taken + 1
    d = d + 1
    if d == len(directions):
        d = 0
    if steps_taken%1000000 == 0:
        print('At nodes ' + str(current_nodes) + ' after taking ' + str(steps_taken) + ' steps')

print('At nodes ' + str(current_nodes) + ' after taking ' + str(steps_taken) + ' steps')
