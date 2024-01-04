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


## INPUT READING FUNCTIONS ##
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