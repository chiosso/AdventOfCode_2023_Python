import itertools

## PROCESS INPUT ##

input = open('test_input.txt', 'r').readlines()

## FUNCTIONS ##

def getQuestionMarkIndexes(s):
    indexes = []
    previous_index = -1
    while True:
        if len(indexes) > 0:
            previous_index = indexes[-1]
        i = s.find('?',previous_index+1)
        if i != -1:
            indexes.append(i)
        else:
            break
    return indexes

def doesSpringCombinationWork(springs, groups):
    groups_counted = 0
    spring_groups = springs.split('.')
    for spring_group in spring_groups:
        if spring_group != '':
            if len(spring_group) != groups[groups_counted]:
                return False
            groups_counted = groups_counted + 1
    return True


## PROCESSING ##

sum_of_possible_arrangements = 0
for line in input:
    components = line.split()
    springs = components[0]
    groups = list(map(int, components[1].split(',')))
    q_indexes = getQuestionMarkIndexes(springs)
    number_known_damaged = springs.count('#')
    springs_base = springs.replace('?','.')
    possible_damaged_spring_combinations = list(itertools.combinations(q_indexes, sum(groups) - number_known_damaged))
    number_possible_arrangements = 0
    for possible_damaged_spring_combination in possible_damaged_spring_combinations:
        springs_candidate = ''
        for i in range(len(springs_base)):
            if i in possible_damaged_spring_combination:
                springs_candidate = springs_candidate + '#'
            else:
                springs_candidate = springs_candidate + springs_base[i]
        if doesSpringCombinationWork(springs_candidate, groups):
            number_possible_arrangements = number_possible_arrangements + 1
    print(springs + ' - ' + str(number_possible_arrangements) + ' arrangements')
    sum_of_possible_arrangements = sum_of_possible_arrangements + number_possible_arrangements
print('Total arrangements: ' + str(sum_of_possible_arrangements))
