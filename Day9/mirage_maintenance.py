def generateDifferencesSequence(sequence):
    differences = []
    for i in range(len(sequence) - 1):
        differences.append(sequence[i+1] - sequence[i])
    return differences


input = open('input.txt','r').readlines()
summed_next_values = 0
summed_previous_values = 0

for line in input:
    sequences = []
    sequences.append(list(map(int, line.split())))
    # Generate the differences sequences until values all same
    while True:
        differences = generateDifferencesSequence(sequences[-1])
        sequences.append(differences)
        if len(set(differences)) == 1:
            break
    # Work backwards through sequences generating next value and previous value
    for i in range(len(sequences)).__reversed__():
        if i == len(sequences)-1:
            sequences[i].append(sequences[i][-1])
            sequences[i].insert(0,sequences[i][0])
        else:
            sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])
            sequences[i].insert(0, sequences[i][0] - sequences[i+1][0])
    print('Sequence: ')
    for sequence in sequences:
        print('\t' + str(sequence))
    summed_next_values = summed_next_values + sequences[0][-1]
    summed_previous_values = summed_previous_values + sequences[0][0]

print('Summed next vals: ' + str(summed_next_values))
print('Summed previous vals: ' + str(summed_previous_values))