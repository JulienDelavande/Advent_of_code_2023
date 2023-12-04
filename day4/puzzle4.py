out = open("output.txt", "w")

with open("input.txt") as f:
    points_sum = 0
    for line in f.readlines():
        winning_numbers = line.split(": ")[1].split(" |")[0].split(" ")
        winning_numbers = [int(i) for i in winning_numbers if i != ""]
        throw_numbers = line.split(": ")[1].split("| ")[1].split(" ")
        throw_numbers = [int(i) for i in throw_numbers if i != ""]
        number_of_winning_numbers = 0
        for number in throw_numbers:        
            if number in winning_numbers:
                number_of_winning_numbers += 1
        if number_of_winning_numbers > 0:
            points_sum += 2**(number_of_winning_numbers-1)
    print(f'Points sum puzzle 4.1: {points_sum}')
out.close()

with open("input.txt") as f:
    scratchcards_number = [1]*len(f.readlines())
    f.seek(0)
    line_number = 0
    for line in f.readlines():
        winning_numbers = line.split(": ")[1].split(" |")[0].split(" ")
        winning_numbers = [int(i) for i in winning_numbers if i != ""]
        throw_numbers = line.split(": ")[1].split("| ")[1].split(" ")
        throw_numbers = [int(i) for i in throw_numbers if i != ""]
        number_of_winning_numbers = 0
        for number in throw_numbers:        
            if number in winning_numbers:
                number_of_winning_numbers += 1
        if number_of_winning_numbers > 0:
            for i in range(1, number_of_winning_numbers + 1):
                scratchcards_number[line_number + i] += scratchcards_number[line_number]
        line_number += 1
    sum_of_scratchcards = sum(scratchcards_number)
    print(f'Sum of scratchcards puzzle 4.2: {sum_of_scratchcards}')