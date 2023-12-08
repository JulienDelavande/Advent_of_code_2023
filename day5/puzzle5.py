with open("input.txt", 'r') as f:
    line = f.readline()
    seeds = line.replace("\n", "").split(" ")[1:]
    maps = []
    maps_name = []
    map = []
    f.readline()
    maps_name.append(f.readline().split(" ")[0])
    for line in f.readlines():
        if "map" in line:
            maps.append(map)
            maps_name.append(line.split(" ")[0])
            map = []
        elif line != "\n":
            map.append(line.replace("\n", "").split(" "))
    maps.append(map)
    print(maps_name)
    print(maps[0])

    print(f"map {maps_name}")

    seeds_current = seeds
    print(seeds_current)
    for i, map in enumerate(maps):
        seeds_new = []
        print(f"map {maps_name[i]}")
        for seed in seeds_current:
            is_mapped = False
            for line in map:
                for destination, start, range in map:
                    start = int(start)
                    range = int(range)
                    seed = int(seed)
                    destination = int(destination)
                    if start <= seed <= start + range:
                        seeds_new.append(destination+seed-start)
                        is_mapped = True
                        break
                if is_mapped:
                    break
            if not is_mapped:
                seeds_new.append(seed)
        print(seeds_new)
        seeds_current = seeds_new
    
    print(min(seeds_current))