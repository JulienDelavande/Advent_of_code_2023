with open("input.txt") as f:
    steps = f.readline().replace("\n", "")
    f.readline()
    nodes = {}
    for line in f.readlines():
        node_start, node_arrival = line.replace("\n", "").split(" = ")
        nodes[node_start] = node_arrival.replace("(", "").replace(")", "").split(", ")

    step_nb = 0
    node_current = "AAA"
    node_stop = "ZZZ"
    while node_current != node_stop:
        if steps[step_nb % len(steps)] == "L":
            node_current = nodes[node_current][0]
        else:
            node_current = nodes[node_current][1]
        step_nb += 1
    print(step_nb)