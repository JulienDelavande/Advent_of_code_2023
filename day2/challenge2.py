output = open("output.txt", "w")

with open("input.txt", "r") as f:
    sum = 0
    for line in f.readlines():
        game_nb = line.split(":")[0].split(" ")[1]
        game_possible = True
        games_results = line.split(": ")[1].split("; ")
        for throw in games_results:
            num_and_colors = throw.split(", ")
            for num_and_color in num_and_colors:
                num = int(num_and_color.split(" ")[0])
                color = num_and_color.split(" ")[1].replace("\n", "")
                if color == "red" and num > 12:
                    game_possible = False
                    #output.write(f'{game_nb}: {game_possible}, sum : {sum}, red={num}\n')
                    break
                if color == "green" and num > 13:
                    game_possible = False
                    #output.write(f'{game_nb}: {game_possible}, sum : {sum}, green={num}\n')
                    break
                if color == "blue" and num > 14:
                    game_possible = False
                    #output.write(f'{game_nb}: {game_possible}, sum : {sum}, blue={num}\n')
                    break
        if game_possible:
            sum += int(game_nb)
            #output.write(f'{game_nb}: {game_possible}, sum : {sum}\n')
        output.write(f'{game_nb}: {game_possible}, sum : {sum}\n')
    print(sum)


with open("input.txt", "r") as f:
    sum = 0
    for line in f.readlines():
        game_nb = line.split(":")[0].split(" ")[1]
        games_results = line.split(": ")[1]
        colors_max = {"red": 0, "green": 0, "blue": 0}
        for throw in games_results.split("; "):
            num_and_colors = throw.split(", ")
            for num_and_color in num_and_colors:
                num = int(num_and_color.split(" ")[0])
                color = num_and_color.split(" ")[1].replace("\n", "")
                if colors_max[color] < num:
                    colors_max[color] = num
        power_of_cubes = 1
        for color in colors_max.keys():
            power_of_cubes *= colors_max[color]
        sum += power_of_cubes
        #output.write(f'{game_nb}: {game_possible}, sum : {sum}, red={colors_sum["red"]}, green={colors_sum["green"]}, blue={colors_sum["blue"]}\n')
    print(sum)

                    
       
