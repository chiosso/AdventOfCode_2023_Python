time = 48989083
distance_record = 390110311121360


winning_hold_times = 0
for hold_time in range(1,time):
    distance_travelled = hold_time * (time - hold_time)
    #if hold_time%100000 == 0:
    #    print('Proceessed ' + str(hold_time))
    if distance_travelled > distance_record:
        print('First winning hold time ' + str(hold_time) + ', disance travelled ' + str(distance_travelled))
        print('Number winning hold times: ' + str(time - hold_time - hold_time + 1))
        break
