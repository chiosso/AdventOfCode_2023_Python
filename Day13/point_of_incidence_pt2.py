import point_of_incidence_functions as poi
DEBUG_OUTPUT = False

input = open('input.txt', 'r')
summarised_notes = 0

while True:
    pattern = poi.getNextPattern(input)
    if len(pattern) == 0:
        break

    print('\nPATTERN: ' + str(pattern))

    # Vertical reflection
    print('Vertical reflection')
    valid_reflection_index_counts = {}
    pattern_height = len(pattern)
    for line in pattern:
        valid_reflection_indexes = poi.findValidReflectionIndexes(line)
        for i in valid_reflection_indexes:
            if i in valid_reflection_index_counts.keys():
                valid_reflection_index_counts[i] += 1
            else:
                valid_reflection_index_counts[i] = 1
    for i in valid_reflection_index_counts.keys():
        if valid_reflection_index_counts[i] == pattern_height - 1:
            print('Valid vertical reflection index: ' + str(i))
            summarised_notes += i + 1

    # Horizontal reflection
    print('Horizontal reflection')
    valid_reflection_index_counts = {}
    pattern_width = len(pattern[0])
    for i in range(len(pattern[0])):
        vertical_string = poi.getVerticalString(pattern,i)
        valid_reflection_indexes = poi.findValidReflectionIndexes(vertical_string)
        for i in valid_reflection_indexes:
            if i in valid_reflection_index_counts.keys():
                valid_reflection_index_counts[i] += 1
            else:
                valid_reflection_index_counts[i] = 1
    for i in valid_reflection_index_counts.keys():
        if valid_reflection_index_counts[i] == pattern_width - 1:
            print('Valid horizontal reflection index: ' + str(i))
            summarised_notes += (i + 1)*100

print('Got to end, summarised notes: ' + str(summarised_notes))
