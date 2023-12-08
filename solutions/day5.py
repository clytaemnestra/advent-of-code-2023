import multiprocessing
import os
import re

from tqdm import tqdm


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
    (
        seeds,
        seed_to_soil_map,
        soil_to_fertilizer_map,
        fertilizer_to_water_map,
        water_to_light_map,
        light_to_temperature_map,
        temperature_to_humidity_map,
        humidity_to_location_map,
    ) = read_data()
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


def process_seed(seed_data, data):
    seed, range_length = seed_data
    smallest_local = float("inf")

    (
        _,
        seed_to_soil_map,
        soil_to_fertilizer_map,
        fertilizer_to_water_map,
        water_to_light_map,
        light_to_temperature_map,
        temperature_to_humidity_map,
        humidity_to_location_map,
    ) = read_data()

    for seed in tqdm(range(seed, seed + range_length)):
        soil = check_location_in_map(seed, seed_to_soil_map)
        fertilizer = check_location_in_map(soil, soil_to_fertilizer_map)
        water = check_location_in_map(fertilizer, fertilizer_to_water_map)
        light = check_location_in_map(water, water_to_light_map)
        light_to_temp = check_location_in_map(light, light_to_temperature_map)
        temperature = check_location_in_map(light_to_temp, temperature_to_humidity_map)
        humidity = check_location_in_map(temperature, humidity_to_location_map)

        if humidity < smallest_local:
            smallest_local = humidity

    return smallest_local


def part2():
    with open("./data/5.txt") as f:
        data = f.read()

    seeds = [int(seed) for seed in re.search(r"seeds: ([\d\s]+)", data).group(1).split()]
    seed_data = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

    with multiprocessing.Pool(processes=os.cpu_count()) as pool:
        smallest_values = pool.starmap(process_seed, [(sd, data) for sd in seed_data])

    return min(smallest_values)


part1()
part2()
