import re
import multiprocessing
import time
import concurrent.futures

def extract(data, map_name):
    map_pattern = r"(\d+)\s+(\d+)\s+(\d+)"
    map_data = re.findall(f"{map_name} map:\n(({map_pattern}\n?)+)", data)

    return [
        tuple(map(int, match.split())) for match in map_data[0][0].split("\n") if match
    ]


def check_location_in_map(i, map):
    for destination_range, source_range, range_length in map:
        if source_range <= i < source_range + range_length:
            return destination_range + (i - source_range)
    return i


def read_data():
    with open("./data/5.txt") as f:
        data = f.read()

        seed_pattern = r"seeds: ([\d\s]+)"
        seeds = [int(seed) for seed in re.search(seed_pattern, data).group(1).split()]

        return (
            seeds,
            extract(data, "seed-to-soil"),
            extract(data, "soil-to-fertilizer"),
            extract(data, "fertilizer-to-water"),
            extract(data, "water-to-light"),
            extract(data, "light-to-temperature"),
            extract(data, "temperature-to-humidity"),
            extract(data, "humidity-to-location"),
        )


def part1():
    seeds, seed_to_soil_map, soil_to_fertilizer_map, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map = (
        read_data()
    )
    locations = []
    for seed in seeds:
        soil = check_location_in_map(seed, seed_to_soil_map)
        fertilizer = check_location_in_map(soil, soil_to_fertilizer_map)
        water = check_location_in_map(fertilizer, fertilizer_to_water_map)
        light = check_location_in_map(water, water_to_light_map)
        light_to_temp = check_location_in_map(light, light_to_temperature_map)
        temperature = check_location_in_map(light_to_temp, temperature_to_humidity_map)
        humidity = check_location_in_map(temperature, humidity_to_location_map)
        locations.append(humidity)
    return min(locations)


def process_seed(seed_data, data, map_pattern):
    seed, range_length = seed_data
    smallest_local = float("inf")

    def _extract(data, map_name, map_pattern):
        map_data = re.findall(f"{map_name} map:\n(({map_pattern}\n?)+)", data)
        return [
            tuple(map(int, match.split()))
            for match in map_data[0][0].split("\n")
            if match
        ]

    def _check_location_in_map(i, map_data):
        for destination_range, source_range, range_length in map_data:
            if source_range <= i < source_range + range_length:
                return destination_range + (i - source_range)
        return i

    for seed in range(seed, seed + range_length):
        print("diff: ", seed + range_length - seed)
        soil = _check_location_in_map(seed, _extract(data, "seed-to-soil", map_pattern))
        fertilizer = _check_location_in_map(
            soil, _extract(data, "soil-to-fertilizer", map_pattern)
        )
        water = _check_location_in_map(
            fertilizer, _extract(data, "fertilizer-to-water", map_pattern)
        )
        light = _check_location_in_map(
            water, _extract(data, "water-to-light", map_pattern)
        )
        light_to_temp = _check_location_in_map(
            light, _extract(data, "light-to-temperature", map_pattern)
        )
        temperature = _check_location_in_map(
            light_to_temp, _extract(data, "temperature-to-humidity", map_pattern)
        )
        humidity = _check_location_in_map(
            temperature, _extract(data, "humidity-to-location", map_pattern)
        )

        if humidity < smallest_local:
            smallest_local = humidity

    return smallest_local


def read_data2():
    with open("./data/5.txt") as f:
        data = f.read()
    seed_pattern = r"seeds: ([\d\s]+)"
    map_pattern = r"(\d+)\s+(\d+)\s+(\d+)"
    seeds = [int(seed) for seed in re.search(seed_pattern, data).group(1).split()]


    seed_data = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

    with multiprocessing.Pool(processes=16) as pool:
        smallest_values = pool.starmap(
            process_seed, [(sd, data, map_pattern) for sd in seed_data]
        )

    return min(smallest_values)


if __name__ == "__main__":
    smallest_humidity = read_data2()
    print(f"The smallest humidity value is: {smallest_humidity}")
