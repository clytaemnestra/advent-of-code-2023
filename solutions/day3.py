def open_data():
    with open("./data/3.txt") as f:
        data = f.read()
        return [l for l in data.split("\n")]


def get_surrounding_area(
    line_index, char_index, matrix, two_digit=False, three_digit=False
):
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    surrounding_chars = []
    rows = len(matrix)
    cols = len(matrix[0])

    col_span = 1
    if two_digit:
        col_span = 2
    elif three_digit:
        col_span = 3

    for offset in offsets:
        for i in range(col_span):
            new_row, new_col = line_index + offset[0], char_index + offset[1] + i
            if 0 <= new_row < rows and 0 <= new_col < cols:
                surrounding_chars.append(matrix[new_row][new_col])
    return surrounding_chars


def check_special_characters_in_area(surrounding_area):
    special_chars = ["*", "#", "@", "/", "&", "+", "=", "%", "$", "-"]
    for ch in surrounding_area:
        if ch in special_chars:
            return True
    return False


def calculate_part_one():
    matrix = open_data()
    nums = []
    for line_index, line in enumerate(matrix):
        for char_index, char in enumerate(line):
            # one digit only
            if (
                char.isdigit()
                and char_index + 1 < len(line)
                and not line[char_index + 1].isdigit()
                and not line[char_index - 1].isdigit()
            ):
                surr = get_surrounding_area(line_index, char_index, matrix)
                if check_special_characters_in_area(surr):
                    nums.append(int(char))
            # two digits
            if (
                char.isdigit()
                and char_index + 1 < len(line)
                and line[char_index + 1].isdigit()
                and char_index + 2 < len(line)
                and not line[char_index + 2].isdigit()
                and not line[char_index - 1].isdigit()
            ):
                surr = get_surrounding_area(
                    line_index, char_index, matrix, two_digit=True
                )
                first_char = char
                second_char = line[char_index + 1]
                if check_special_characters_in_area(surr):
                    nums.append(int(first_char + second_char))
            # three digits
            if (
                char.isdigit()
                and char_index + 1 < len(line)
                and line[char_index + 1].isdigit()
                and char_index + 2 < len(line)
                and line[char_index + 2].isdigit()
                and not line[char_index - 1].isdigit()
            ):
                surr = get_surrounding_area(
                    line_index, char_index, matrix, three_digit=True
                )
                first_char = char
                second_char = line[char_index + 1]
                third_char = line[char_index + 2]
                if check_special_characters_in_area(surr):
                    nums.append(int(first_char + second_char + third_char))
    return sum(nums)


def calculate_part_two():
    matrix = open_data()
    m = []
    rows = len(matrix)
    cols = len(matrix[0])
    for line_index, line in enumerate(matrix):
        for char_index, char in enumerate(line):
            if char == "*":
                nums = []
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ni, nj = line_index + di, char_index + dj
                        if (
                            0 <= ni < rows
                            and 0 <= nj < cols
                            and matrix[ni][nj].isdigit()
                        ):
                            while nj > 0 and matrix[ni][nj - 1].isdigit():
                                nj -= 1
                            number = ""
                            while nj < cols and matrix[ni][nj].isdigit():
                                number += matrix[ni][nj]
                                nj += 1
                            if number:
                                nums.append(int(number))
                if len(set(nums)) >= 2:
                    result = 1
                    for i in set(nums):
                        result *= i
                    m.append(result)
    return sum(m)


calculate_part_one()
calculate_part_two()
