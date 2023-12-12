with open("input.txt") as f:
    lines = [[int(number) for number in line.split()] for line in f.readlines()]
    predicted_numbers = []
    for line in lines:
        descent = [line]

        while descent[-1] != [0]*len(descent[-1]):
            descent.append([descent[-1][i] - descent[-1][i-1] for i in range(1, len(descent[-1]))])
        predicted_number = sum([descent[i][-1] for i in range(len(descent))])
        predicted_numbers.append(predicted_number)
    print(sum(predicted_numbers))