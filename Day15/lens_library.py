def hash(s):
    current_value = 0
    for c in s:
        current_value = (current_value + ord(c))*17%256
    return current_value


input = open('input.txt', 'r').readline().split(',')

sum_of_hashes = 0
for s in input:
    sum_of_hashes += hash(s.strip())

print('Sum of hashes = ' + str(sum_of_hashes))