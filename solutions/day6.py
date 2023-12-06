def calculate_ways_to_win(races):
    total_ways = 1
    for time, distance in races:
        way_to_win = 0
        for j in range(0, time + 1):
            go = (time - j) * j if time != 0 else 0
            if go > distance:
                way_to_win += 1
        total_ways = total_ways * way_to_win

    return total_ways


calculate_ways_to_win(races=[(46689866, 358105418071080)])
