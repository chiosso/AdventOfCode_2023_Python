import point_of_incidence_functions as poi
DEBUG_OUTPUT = False

input = open('input.txt', 'r')
summarised_notes = 0

while True:
    pattern = poi.getNextPattern(input)
    if len(pattern) == 0:
        break

    print('\nPATTERN: ' + str(pattern))
    # Check for vertical reflection
    valid_reflection_indexes = poi.findValidReflectionIndexes(pattern[0])
    if DEBUG_OUTPUT:
        print('First line valid vertical reflection indexes: ' + str(valid_reflection_indexes))
    for line in range(1,len(pattern)):
        invalid_reflection_indexes = set()
        for i in valid_reflection_indexes:
            if poi.isStringSymmetrical(pattern[line],i) == False:
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
    valid_reflection_indexes = poi.findValidReflectionIndexes(poi.getVerticalString(pattern,0))
    if DEBUG_OUTPUT:
        print('First line valid horizontal reflection indexes: ' + str(valid_reflection_indexes))
    for col in range(1, len(pattern[0])):
        vertical_string = poi.getVerticalString(pattern, col)
        invalid_reflection_indexes = set()
        for i in valid_reflection_indexes:
            if poi.isStringSymmetrical(vertical_string, i) == False:
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
