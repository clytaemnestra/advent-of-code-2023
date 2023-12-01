def part1():
    with open("./data/1.txt") as f:
        data = f.read()
        sum = 0
        for line in data.split("\n"):
            first = None
            last = None
            for l in line:
                if l.isdigit():
                    if first is None:
                        first = l
                    last = l
            number = str(first) + str(last)
            sum += int(number)
        return print(sum)


def part2():
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    with open("./data/1.txt") as f:
        data = f.read()
        sum = 0
        for line in data.split("\n"):
            l = []
            for i in range(len(line)):
                if line[i].isdigit():
                    l.append(int(line[i]))
                for j in range(i + 1, len(line) + 1):
                    substring = line[i:j]
                    if substring in numbers:
                        first = numbers.get(substring)
                        l.append(first)
            number = str(l[0]) + str(l[-1])
            sum += int(number)
        return sum


part1()
part2()
