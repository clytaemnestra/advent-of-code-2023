import re
from collections import defaultdict
from functools import cache


def read_data():
    with open("./data/4.txt") as f:
        data = f.read()
        for line in data.split("\n"):
            return [
                (
                    (
                        tuple(
                            int(i)
                            for i in re.search(r"(?<=:)\s*(\d+(?:\s+\d+)*)\s*\|", line)
                            .group(1)
                            .split()
                        ),
                        tuple(
                            int(j)
                            for j in re.search(r"(?<=\|)\s*(\d+(?:\s+\d+)*)", line)
                            .group(1)
                            .split()
                        ),
                    )
                )
                for line in data.split("\n")
            ]


@cache
def calculate_points(x):
    if x <= 2:
        return x
    else:
        return 2 * calculate_points(x - 1)


def calculate_part_one():
    cards = read_data()
    sum = 0
    for card in cards:
        points = calculate_points((len(set(card[0]).intersection(card[1]))))
        sum += points
    return sum


def calculate_part_two():
    cards = read_data()
    cards_with_instances = defaultdict(int)
    for index, card in enumerate(cards, start=1):
        points = len(set(card[0]).intersection(card[1]))
        cards_with_instances[index] += 1
        for j in range(cards_with_instances[index]):
            for k in range(1, points + 1):
                cards_with_instances[index + k] += 1
    return sum(cards_with_instances.values())


calculate_part_one()
calculate_part_two()
