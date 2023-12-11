time = [7,15,30]
distance_record = [9,40,200]
number_winning_hold_times = []

for race in range(0,len(time)):
    winning_hold_times = []
    for hold_time in range(1,time[race]):
        distance_travelled = hold_time * (time[race] - hold_time)
        print('Hold time ' + str(hold_time) + ', disance travelled ' + str(distance_travelled))
        if distance_travelled > distance_record[race]:
            winning_hold_times.append(hold_time)
    print('Race ' + str(race+1) + ': ' + str(len(winning_hold_times)) + ' winning hold times: ' + str(winning_hold_times))
    number_winning_hold_times.append(len(winning_hold_times))


print('Number winning hold times: ' + str(number_winning_hold_times))
answer = 1
for i in number_winning_hold_times:
    answer = answer * i
print('Answer: ' + str(answer))
