with open('input.txt') as f:

    times = f.readline().replace("\n", "").split(':')[1].split()
    distances = f.readline().replace("\n", "").split(':')[1].split()
    times = [int(i) for i in times]
    distances = [int(i) for i in distances]

    ways_to_beat = [0]*len(times)

    for race_nb in range(len(times)):
        for acc_time in range(times[race_nb]):
            distance = acc_time*(times[race_nb]-acc_time)
            if distance > distances[race_nb]:
                ways_to_beat[race_nb] += 1
    
    ways_to_beat_multiplied = 1
    for i in ways_to_beat:
        ways_to_beat_multiplied *= i
    
    print(ways_to_beat_multiplied)
