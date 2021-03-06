import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

starting_numbers = all_lines[0].split(",")
starting_numbers = [int(s) for s in starting_numbers]

spoken_numbers = {}

for i in range(len(starting_numbers)):
    spoken_numbers[starting_numbers[i]] = i + 1

current_number = 0
spoken_numbers[current_number] = len(starting_numbers) + 1
current_number = 4

for i in range(len(spoken_numbers) + 2, 30000001):
    current_number_index = spoken_numbers.get(current_number, i)

    if not current_number_index == i:
        old_current_number = current_number
        current_number = i - current_number_index
        spoken_numbers[old_current_number] = i
    else:
        spoken_numbers[current_number] = i
        current_number = 0


print(list(spoken_numbers.keys())[list(spoken_numbers.values()).index(30000000)])
