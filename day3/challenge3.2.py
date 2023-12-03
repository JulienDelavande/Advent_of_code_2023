out = open("output.txt", "w")
out2 = open("output2.txt", "w")
out3 = open("output3.txt", "w")
output_num_to_sum = open("output_num_to_sum.txt", "w")


with open("input.txt", "r") as f:
    sum = 0
    symbol_pos = []
    for line in f.readlines():
        symbol_pos_line = []
        for letter_idx in range(len(line)):
            if line[letter_idx] == "*":
                symbol_pos_line.append(letter_idx)
        symbol_pos.append(symbol_pos_line)
        out.write(f'{symbol_pos_line}\n')
    numbers = []
    number_pos = []
    f.seek(0)
    for line in f.readlines():
        numbers_line = []
        number_pos_line = []
        last_number = 0
        number_pos_line_idx = []
        for letter_idx in range(len(line)):
            current_letter = line[letter_idx]
            if current_letter.isnumeric():
                last_number = last_number * 10 + int(current_letter)
                number_pos_line_idx.append(letter_idx)
            else:
                if last_number != 0:
                    numbers_line.append(last_number)
                    number_pos_line.append(number_pos_line_idx)
                number_pos_line_idx = []
                last_number = 0
        numbers.append(numbers_line)
        number_pos.append(number_pos_line)
        out2.write(f'{numbers_line}\n')
        out3.write(f'{number_pos_line}\n')

    sum = 0
    for line_idx in range(len(numbers)):
        numbers_to_sum = []
        for stars_idx in range(len(symbol_pos[line_idx])):
            adjacent_numbers = []
            line_of_symbol_pos = symbol_pos[line_idx]
            for num_line_idx in range(len(numbers[line_idx])):
                num = numbers[line_idx][num_line_idx]
                num_pos_line_idx = number_pos[line_idx][num_line_idx]
                for digit_pos in num_pos_line_idx:
                    if abs(digit_pos - line_of_symbol_pos[stars_idx]) < 2:
                        adjacent_numbers.append(num)
                        break
            if line_idx != 0:
                line_above_symbol_pos = symbol_pos[line_idx - 1]
                for num_line_idx in range(len(numbers[line_idx - 1])):
                    num = numbers[line_idx - 1][num_line_idx]
                    num_pos_line_idx = number_pos[line_idx - 1][num_line_idx]
                    for digit_pos in num_pos_line_idx:
                        if abs(digit_pos - line_of_symbol_pos[stars_idx]) < 2:
                            adjacent_numbers.append(num)
                            break
            if line_idx != len(numbers) - 1:
                line_below_symbol_pos = symbol_pos[line_idx + 1]
                for num_line_idx in range(len(numbers[line_idx + 1])):
                    num = numbers[line_idx + 1][num_line_idx]
                    num_pos_line_idx = number_pos[line_idx + 1][num_line_idx]
                    for digit_pos in num_pos_line_idx:
                        if abs(digit_pos - line_of_symbol_pos[stars_idx]) < 2:
                            adjacent_numbers.append(num)
                            break
            if len(adjacent_numbers) > 1:
                star_mult = 1
                for num in adjacent_numbers:
                    star_mult *= num
                sum += star_mult
    print(sum)
