import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')

min_wait = int(all_lines[0])
buses = all_lines[1].split(",")
buses = [item for item in buses if item != "x"]

max_waits = [range(len(buses))]

for i in range(len(max_waits)):
    max_waits[i] = buses[i]