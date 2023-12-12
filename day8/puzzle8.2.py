from math import lcm

with open("input.txt") as f:
    steps = f.readline().replace("\n", "")
    f.readline()
    nodes = {}
    for line in f.readlines():
        node_start, node_arrival = line.replace("\n", "").split(" = ")
        nodes[node_start] = node_arrival.replace("(", "").replace(")", "").split(", ")

    nodes_starts = [node for node in nodes.keys() if node[2] == "A"]
    nodes_stop = [node for node in nodes.keys() if node[2] == "Z"]

    print(nodes_starts)
    print(nodes_stop)
    print(len(steps))
    steps_all_nodes = []

    for node_start in nodes_starts:
        step_nb = 0
        node_current = node_start
        stop = False

        while not stop:

            if steps[step_nb % len(steps)] == "L":
                node_current = nodes[node_current][0]
            else:
                node_current = nodes[node_current][1]
            
            step_nb += 1

            if node_current[2] == "Z":
                print(step_nb)
                steps_all_nodes.append(step_nb)
                stop = True
            
    # compute ppcm steps_all_nodes
    print(steps_all_nodes)
    lcm_ = lcm(steps_all_nodes[0], steps_all_nodes[1])
    for node_nb in range(2, len(steps_all_nodes)):
        lcm_ = lcm(lcm_, steps_all_nodes[node_nb])
    print(lcm_)
