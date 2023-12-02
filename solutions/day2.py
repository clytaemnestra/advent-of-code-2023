import re


def part1():
    with open("./data/2.txt") as f:
        data = f.read()
        lines = [line.replace(",", "").strip() for line in data.split("\n")]
        games_dict = {}
        for l in lines:
            pattern = f"Game (\d+)"
            match = re.search(pattern, l)
            num = int(match.group(1))
            games_dict[num] = l[3:]
        for i, z in games_dict.items():
            segments = z.split(";")
            all_segments = []
            for segment in segments:
                matches = re.findall(r"(\d+) (\w+)", segment)
                color_list = [{int(number): color} for number, color in matches]
                all_segments.append(color_list)
            games_dict[i] = all_segments
        game_id_sum = 0
        for k, v in games_dict.items():
            above_limit = False
            for l in v:
                for t in l:
                    for j, m in t.items():
                        if m == "red" and j > 12:
                            above_limit = True
                        elif m == "blue" and j > 14:
                            above_limit = True
                        elif m == "green" and j > 13:
                            above_limit = True
            if not above_limit:
                game_id_sum += k
        return game_id_sum


def part2():
    with open("./data/2.txt") as f:
        data = f.read()
        lines = [
            line.replace(",", "").replace(";", "").strip() for line in data.split("\n")
        ]
        games_dict = {}
        for l in lines:
            pattern = f"Game (\d+)"
            match = re.search(pattern, l)
            num = int(match.group(1))
            games_dict[num] = l[3:]
        for i, z in games_dict.items():
            matches = re.findall(r"(\d+) (\w+)", z)
            color_list = [{int(number): color} for number, color in matches]
            games_dict[i] = color_list
        sum = 0
        for k, v in games_dict.items():
            highest_red = 0
            highest_blue = 0
            highest_green = 0
            for i in v:
                for m, n in i.items():
                    if n == "red" and m > highest_red:
                        highest_red = m
                    if n == "blue" and m > highest_blue:
                        highest_blue = m
                    if n == "green" and m > highest_green:
                        highest_green = m
            power = highest_red * highest_green * highest_blue
            sum += power
        return sum


part1()
part2()
