import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

with open(file_path, 'r') as input:
    all_lines = input.readlines()

starting_numbers = all_lines[0].split(",")
starting_numbers = [int(s) for s in starting_numbers]

spoken_numbers = []

for number in starting_numbers:
    spoken_numbers.append(number)

spoken_numbers.append(0)


def guess_seq_len(seq):
    guess = 1
    max_len = int(len(seq) / 2)
    for x in range(2, max_len):
        if seq[0:x] == seq[x:2*x] :
            return x

    return guess


for i in range(len(spoken_numbers), 30000000):
    last_number = spoken_numbers[len(spoken_numbers) - 1]
    temp_spoken_numbers = spoken_numbers[:len(spoken_numbers) - 1]

    if last_number in temp_spoken_numbers:
        spoken_numbers.append(i - (len(temp_spoken_numbers) - temp_spoken_numbers[::-1].index(last_number)))
    else:
        spoken_numbers.append(0)

    seq_len = guess_seq_len(spoken_numbers)
    if not seq_len == 1:
        print(spoken_numbers[:seq_len - 1])

print(spoken_numbers[30000000 - 1])
