# Advent of Code
# Day 9
# https://adventofcode.com/2024/day/9

file = open("./Day_09/input.txt", "r")
input = file.readlines()[0].rstrip("\n")

memory = []     # [data, index], [ , ]
data = True
j = 0
for i in range(len(input)):
    if data:
        memory.append([int(input[i]) * str(j%10), j])
        j += 1
    else:
        if int(input[i]) != 0:
            memory.append([int(input[i]) * ".", "."])
    data = not data

memory2 = []
for cell in memory:
    for data in cell[0]:
        memory2.append([data, cell[1]])

j = len(memory2) - 1
for i in range(len(memory2)):
    if j <= i:
        break
    if memory2[i][0] == ".":
        while memory2[j][0] == ".":
            j -= 1
        memory2[i] = memory2[j]
        memory2[j] = [".", "."]
        j -= 1

checksum = 0
i = 0
for cell in memory2:
    if cell[1] != ".":
        checksum += i * cell[1]
    i += 1
print("First Puzzle:", checksum)


memory3 = []
for cell in memory:
    for data in cell[0]:
        memory3.append([data, cell[1]])

def move_data_if_possible(i):
    data_len = 1
    while memory3[i - data_len][0] == memory3[i][0]:
        data_len += 1

    for j in range(len(memory3)):
        if j >= i:
            return data_len
        free_space_len = 1
        if memory3[j][0] == ".":
            if (j + free_space_len) < len(memory3):
                while memory3[j + free_space_len][0] == ".":
                    free_space_len += 1
                    if (j + free_space_len) >= len(memory3):
                        return data_len
            else:
                return data_len

            if free_space_len >= data_len:
                for l in range(data_len):
                    memory3[j + l] = memory3[i - l]
                    memory3[i - l] = [".", "."]
                return data_len

index = len(memory3) - 1
while index > 0:
    if memory3[index][0] != ".":
        index -= move_data_if_possible(index)
    else:
        index -= 1
    print("\r... {0:2.1f}%".format(100 - (index / len(memory3) * 100)), end="")

checksum2 = 0
i = 0
for cell in memory3:
    if cell[1] != ".":
        checksum2 += i * cell[1]
    i += 1
print("\rSecond Puzzle:", checksum2)
