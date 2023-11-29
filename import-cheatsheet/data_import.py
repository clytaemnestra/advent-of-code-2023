def data_point_per_row():
    """
    input:
    9057
    8878
    2753
    -> split by line

    output:
    [9057, 8878, 2753]
    """
    with open("./data-examples/1.txt") as f:
        data = f.read()
        return [int(line) for line in data.split("\n")]


def multiple_data_points_by_row_comma_separated():
    """
    input:
    9,0,5,7
    8,8,7,8
    2,7,5,3
    -> split by line & comma

    output:
    [(9,0,5,7), (8,8,7,8), (2,7,5,3)]
    """
    with open("./data-examples/2.txt") as f:
        data = f.read()
        return [tuple(map(int, line.split(","))) for line in data.split("\n")]


def multiple_data_points_by_row():
    """
    input:
    9057
    8878
    2753
    -> split by line

    output:
    [(9,0,5,7), (8,8,7,8), (2,7,5,3)]
    """
    with open("./data-examples/1.txt") as f:
        data = f.read()
        return [tuple(map(int, line)) for line in data.split("\n")]


def data_point_split_in_a_row():
    """
    input:
    C Y
    B Z
    C Y
    -> split by empty space & line
    output:

    [('C', 'Y'), ('B', 'Z'), ('C', 'Y')]
    """
    with open("./data-examples/3.txt") as f:
        data = f.read()
        return [tuple(map(str, line.split())) for line in data.split("\n")]
