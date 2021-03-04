import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

for i in range(len(all_lines)):
    all_lines[i] = all_lines[i].strip('\n')

split_all_lines = [[] for i in range(len(all_lines))]

for i in range(len(split_all_lines)):
    split_all_lines[i] = all_lines[i].split(" ")
    split_all_lines[i].remove("=")

# TODO: Look at these to continue implementing the bitmask
# TODO: Recycle stuff from Day_14_1 for parsing and checking
# https://stackoverflow.com/questions/52382444/replace-combinations-of-characters
# https://stackoverflow.com/questions/14841652/string-replacement-combinations