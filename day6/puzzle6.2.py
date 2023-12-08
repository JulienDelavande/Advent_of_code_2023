with open('input.txt') as f:

    time = f.readline().replace("\n", "").split(':')[1].replace(" ", "")
    distance = f.readline().replace("\n", "").split(':')[1].replace(" ", "")
    time = int(time)
    distance_max = int(distance)

    ways_to_beat = 0

    for acc_time in range(time):
        distance = acc_time*(time-acc_time)
        if distance > distance_max:
            ways_to_beat += 1
    
    print(ways_to_beat)
