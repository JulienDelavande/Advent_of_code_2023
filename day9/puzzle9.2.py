out = open("output.txt", "w")

with open("input.txt") as f:
    lines = [[int(number) for number in line.split()] for line in f.readlines()]
    predicted_numbers = []
    for line in lines:
        descent = [line]

        while descent[-1] != [0]*len(descent[-1]):
            descent.append([descent[-1][i] - descent[-1][i-1] for i in range(1, len(descent[-1]))])
        descent[-1].insert(0, 0)
        for i in range(len(descent)-2, 0, -1):
            descent[i].insert(0, descent[i+1][0] + descent[i][0])

        for j in range(1, len(descent)):
            for i in range(1, len(descent[j])):
                descent[j][i] = descent[j][i-1] + descent[j-1][i]
        predicted_number = sum([descent[i][0] for i in range(len(descent))])
        predicted_numbers.append(predicted_number)
    print(sum(predicted_numbers))