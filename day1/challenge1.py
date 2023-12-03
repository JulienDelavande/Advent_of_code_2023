with open("input.txt") as f:
    somme = 0
    for line in f:
        for letter in line:
            if letter.isnumeric():
                first = letter
                break
        for letter in line[::-1]:
            if letter.isnumeric():
                last = letter
                break
        somme += int(first + last)
    print(somme)
