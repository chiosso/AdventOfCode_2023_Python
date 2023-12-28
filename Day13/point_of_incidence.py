DEBUG_OUTPUT = False

## REFLECTION FUNCTIONS ##

def isStringSymmetrical(s, reflection_index): # Line of reflection is at position after reflection_index
    left_index = reflection_index
    right_index = reflection_index + 1
    while (left_index >= 0 and right_index < len(s)):
        if (s[left_index] != s[right_index]):
            return False
        left_index = left_index - 1
        right_index = right_index + 1
    return True

def findValidReflectionIndexes(s):
    valid_reflection_indexes = []
    for i in range(len(s)-1):
        if isStringSymmetrical(s,i):
            valid_reflection_indexes.append(i)
    return valid_reflection_indexes


## READ INPUT ##

input = open('input.txt', 'r')

def getNextPattern(input):
    pattern = []
    while True:
        line = input.readline().strip()
        if len(line) > 0:
            pattern.append(line)
        else:
            break
    return pattern

def getVerticalString(pattern, col_index):
    s = ''
    for line in pattern:
        s += line[col_index]
    return s

## PROCESS INPUT ##

summarised_notes = 0

while True:
    pattern = getNextPattern(input)
    if len(pattern) == 0:
        break

    print('\nPATTERN: ' + str(pattern))
    # Check for vertical reflection
    valid_reflection_indexes = findValidReflectionIndexes(pattern[0])
    if DEBUG_OUTPUT:
        print('First line valid vertical reflection indexes: ' + str(valid_reflection_indexes))
    for line in range(1,len(pattern)):
        invalid_reflection_indexes = set()
        for i in valid_reflection_indexes:
            if isStringSymmetrical(pattern[line],i) == False:
                invalid_reflection_indexes.add(i)
        if DEBUG_OUTPUT and len(invalid_reflection_indexes) > 0:
            print('Line ' + str(line) + ' removing ' + str(invalid_reflection_indexes))
        for i in invalid_reflection_indexes:
            valid_reflection_indexes.remove(i)
        if len(valid_reflection_indexes) == 0:
            break
    match len(valid_reflection_indexes):
        case 1:
            print('Finished processing pattern. Valid vertical reflection index: ' + str(valid_reflection_indexes[0]))
            summarised_notes += int(valid_reflection_indexes[0]) + 1
        case 0:
            print('Finished processing pattern. No vertical reflection indexes.')
        case _:
            print('ERROR: multiple vertical reflection lines: ' + str(valid_reflection_indexes))


    # Check for horizontal reflection
    valid_reflection_indexes = findValidReflectionIndexes(getVerticalString(pattern,0))
    if DEBUG_OUTPUT:
        print('First line valid horizontal reflection indexes: ' + str(valid_reflection_indexes))
    for col in range(1, len(pattern[0])):
        vertical_string = getVerticalString(pattern, col)
        invalid_reflection_indexes = set()
        for i in valid_reflection_indexes:
            if isStringSymmetrical(vertical_string, i) == False:
                invalid_reflection_indexes.add(i)
        if DEBUG_OUTPUT and len(invalid_reflection_indexes) > 0:
            print('Line ' + str(col) + ' removing ' + str(invalid_reflection_indexes))
        for i in invalid_reflection_indexes:
            valid_reflection_indexes.remove(i)
        if len(valid_reflection_indexes) == 0:
            break
    match len(valid_reflection_indexes):
        case 1:
            print('Finished processing pattern. Valid horizontal reflection index: ' + str(valid_reflection_indexes[0]))
            summarised_notes += 100*(int(valid_reflection_indexes[0])+1)
        case 0:
            print('Finished processing pattern. No horizontal reflection indexes.')
        case _:
            print('ERROR: multiple horizontal reflection lines: ' + str(valid_reflection_indexes))

print('Got to end, summarised notes: ' + str(summarised_notes))
