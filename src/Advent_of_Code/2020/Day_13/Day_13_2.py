import os
import math

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')

split_buses = all_lines[1].split(",")
buses = [item for item in split_buses if item != "x"]
buses = [int(s) for s in buses]

for i in range(len(buses)):
    current_bus = buses[i]
    buses[i] = current_bus, split_buses.index(current_bus)

min_timestamp = math.ceil(100000000000000 / buses[0][0]) * buses[0][0]
