dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}

o = open("output.txt", "w")

def find_all_occurrences(s, sub):
    start = 0
    indices = []
    while True:
        start = s.find(sub, start)
        if start == -1: return indices
        indices.append(start)
        start += len(sub) # use start += 1 to find overlapping matches

with open("input.txt") as f:
    somme = 0
    for line in f:
        numbers = []
        pos = []
        for word in dict.keys():
            if word in line:
                all_occurrences = find_all_occurrences(line, word)
                for occurrence in all_occurrences:
                    pos.append(occurrence)
                    numbers.append(dict[word])
        for letter in line:
            if letter.isnumeric():
                all_occurrences = find_all_occurrences(line, letter)
                for occurrence in all_occurrences:
                    pos.append(occurrence)
                    numbers.append(letter)
        min_index = pos.index(min(pos))
        first = numbers[min_index]
        max_index = pos.index(max(pos))
        last = numbers[max_index]
        o.write(first + last + "\n")
        somme += int(first + last)
    print(somme)
