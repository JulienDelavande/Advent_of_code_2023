def range_intersection_difference(start1, size1, start2, size2):
    end1 = start1 + size1
    end2 = start2 + size2

    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    intersection_size = max(0, intersection_end - intersection_start)

    difference_start = start1
    difference_end = min(end1, start2)
    difference_size = max(0, difference_end - difference_start)

    return intersection_start, intersection_size, difference_start, difference_size

def range_intersection_difference(start1, size1, start2, size2):
    end1 = start1 + size1
    end2 = start2 + size2
    range1 = range(start1, end1)
    range2 = range(start2, end2)

    set1 = set(range1)
    set2 = set(range2)

    intersection = set1.intersection(set2)
    difference = set1.difference(set2)

    intersection_start = min(intersection) if len(intersection) > 0 else 0
    intersection_end = max(intersection) if len(intersection) > 0 else 0
    intersection_size = max(0, intersection_end - intersection_start + 1) if len(intersection) > 0 else 0

    difference_start = min(difference) if len(difference) > 0 else 0
    difference_end = max(difference)    if len(difference) > 0 else 0
    difference_size = max(0, difference_end - difference_start + 1) if len(difference) > 0 else 0

    return intersection_start, intersection_size, difference_start, difference_size

def range_intersection_difference(start1, size1, start2, size2):
    end1 = start1 + size1
    end2 = start2 + size2

    # Calcul de l'intersection
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    intersection_size = max(0, intersection_end - intersection_start)

    # Calcul de la différence
    if start1 < intersection_start:
        difference_start = start1
        difference_end = intersection_start
    elif end1 > intersection_end:
        difference_start = intersection_end
        difference_end = end1
    else:
        # Aucune différence si la première plage est entièrement dans la seconde
        difference_start = 0
        difference_end = 0

    difference_size = max(0, difference_end - difference_start)

    return intersection_start, intersection_size, difference_start, difference_size

def range_intersection_difference(start1, size1, start2, size2):
    end1 = start1 + size1
    end2 = start2 + size2
    difference_start_bis = 0
    difference_end_bis = 0

    if end1 <= start2:
        intersection_start = 0
        intersection_end = 0
        difference_start = start1
        difference_end = end1
        print("end1 < start2")

    if start1<start2 and end1<=end2 and end1>start2:
        intersection_start = start2
        intersection_end = end1
        difference_start = start1
        difference_end = start2
        print("start1<start2 and end1<end2 and end1>start2")

    if start1>=start2 and end1<=end2:
        intersection_start = start1
        intersection_end = end1
        difference_start = 0
        difference_end = 0
        print("start1>=start2 and end1<=end2")

    if start1>=start2 and end1>end2 and start1<end2:
        intersection_start = start1
        intersection_end = end2
        difference_start = end2
        difference_end = end1
        print("start1>start2 and end1>end2 and start1<end2")

    if start1 >= end2:
        intersection_start = 0
        intersection_end = 0
        difference_start = start1
        difference_end = end1
        print("start1 > end1")

    if start1<start2 and end1>end2:
        intersection_start = start2
        intersection_end = end2
        difference_start = start1
        difference_end = start2
        difference_start_bis = end2
        difference_end_bis = end1
        print("start1<start2 and end1>end2")

    print(f"start1:{start1}, end1:{end1}, start2:{start2}, end2:{end2}")
    
    
    intersection_size = intersection_end - intersection_start
    difference_size = difference_end - difference_start
    difference_size_bis = difference_end_bis - difference_start_bis

    return intersection_start, intersection_size, difference_start, difference_size, difference_start_bis, difference_size_bis

    

def merge_ranges(ranges):
    # Trier les plages par leur point de départ
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    merged_ranges = []
    for range_ in sorted_ranges:
        # Si la liste merged_ranges est vide ou si la plage actuelle ne s'intersecte pas avec la dernière plage ajoutée,
        # ajoutez-la simplement à merged_ranges.
        if not merged_ranges or merged_ranges[-1][0] + merged_ranges[-1][1] < range_[0]:
            merged_ranges.append(range_)
        else:
            # Sinon, fusionnez la dernière plage avec la plage actuelle
            last_range_start, last_range_size = merged_ranges[-1]
            current_range_end = max(last_range_start + last_range_size, range_[0] + range_[1])
            merged_ranges[-1] = (last_range_start, current_range_end - last_range_start)

    # supprime les dupplicats
    new_merged_ranges = []
    for range_ in merged_ranges:
        if range_ not in new_merged_ranges:
            new_merged_ranges.append(range)

    return new_merged_ranges



with open("input.txt", 'r') as f:
    line = f.readline()
    seeds = line.replace("\n", "").split(" ")[1:]
    seeds = [(int(seeds[i]), int(seeds[i+1])) for i in range(0, len(seeds) - 1, 2)]

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
            line = line.replace("\n", "").split(" ")
            map.append([int(line[i]) for i in [0, 1, 2]])
    
    maps.append(map)

    print(f"map {maps_name}")

    seeds_current = seeds
    print(seeds_current)
    for i, map in enumerate(maps):
        seeds_new = []
        print(f"map {maps_name[i]}")
        for destination, start, size in map:
            #print(f"destination {destination}, start {start}, range {size}")
            for j, (seed_start, seed_size) in enumerate(seeds_current):
                #print(f"seed_start {seed_start}, seed_size {seed_size}")
                start_intersection, size_intersection, start_difference, size_difference, difference_start_bis, difference_size_bis= range_intersection_difference(seed_start, seed_size, start, size)
                #print(f"start_intersection {start_intersection}, size_intersection {size_intersection}, start_difference {start_difference}, size_difference {size_difference}")
                if size_intersection > 0:
                    seeds_new.append((destination+start_intersection-start, size_intersection))
                seeds_current[j] = (start_difference, size_difference)
                if difference_size_bis > 0:
                    seeds_current.append((difference_start_bis, difference_size_bis))
        for seed_start, seed_size in seeds_current:
            if seed_size > 0:
                seeds_new.append((seed_start, seed_size))
        seed_new = merge_ranges(seeds_new)
        print(seeds_new)
        seeds_current = seeds_new
    
    print(min([start for start, size in seeds_current]))