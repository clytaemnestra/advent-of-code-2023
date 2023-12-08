from collections import Counter

strength = "AKQJT98765432"
strength_with_joker = "AKQT98765432J"


def read_data():
    with open("./data/7.txt") as f:
        data = f.read()
    return [
        (part[0], int(part[1])) for part in (line.split() for line in data.split("\n"))
    ]


def sort_key(hand):
    count = Counter(hand[0])
    sorted_count = sorted(count.values(), reverse=True)
    return tuple(sorted_count)


def compare_hands(hand1, hand2):
    for card1, card2 in zip(hand1, hand2):
        if strength.index(card1) != strength.index(card2):
            return strength.index(card1) > strength.index(card2)
    return False


def sort_hands(sorted_hands):
    i = 0
    while i < len(sorted_hands) - 1:
        current_hand, next_hand = sorted_hands[i], sorted_hands[i + 1]
        if sort_key(current_hand) == sort_key(next_hand):
            if compare_hands(current_hand[0], next_hand[0]):
                sorted_hands[i], sorted_hands[i + 1] = (
                    sorted_hands[i + 1],
                    sorted_hands[i],
                )
                i = max(0, i - 1)
            else:
                i += 1
        else:
            i += 1
    return sorted_hands


def calculate_sum(sorted_hands):
    sum = 0
    for i, j in enumerate(sorted_hands[::-1], start=1):
        sum += i * j[1]
    return sum


def part1():
    hands = read_data()
    sorted_hands = sort_hands(sorted(hands, key=sort_key, reverse=True))
    sum_part_one = calculate_sum(sorted_hands)

    return sum_part_one


part1()
