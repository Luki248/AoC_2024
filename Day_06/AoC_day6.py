# Advent of Code
# Day 6
# https://adventofcode.com/2024/day/6

file = open("./Day_06/input.txt", "r")
input = file.readlines()

grid = []
grid_visits = []
for line in input:
    line = line.rstrip("\n")
    gridline = []
    for chr in line:
        gridline.append(chr)
    grid.append(gridline)
    grid_visits.append(["."]*len(grid[0]))

def search_guard():
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if grid[i][j] == "^":
                return [i, j]

guard_pos = search_guard()

while True:
    grid_visits[guard_pos[0]][guard_pos[1]] = "X"

    try:
        if grid[guard_pos[0]][guard_pos[1]] == "^":
            if guard_pos[0] <= 0:
                break
            if grid[guard_pos[0] - 1][guard_pos[1]] == "#":
                grid[guard_pos[0]][guard_pos[1]] = ">"
        elif grid[guard_pos[0]][guard_pos[1]] == "v":
            if guard_pos[0] > len(grid):
                break
            if grid[guard_pos[0] + 1][guard_pos[1]] == "#":
                grid[guard_pos[0]][guard_pos[1]] = "<"
        elif grid[guard_pos[0]][guard_pos[1]] == "<":
            if guard_pos[1] <= 0:
                break
            if grid[guard_pos[0]][guard_pos[1] - 1] == "#":
                grid[guard_pos[0]][guard_pos[1]] = "^"
        else:   # ">"
            if guard_pos[1] > len(grid[0]):
                break
            if grid[guard_pos[0]][guard_pos[1] + 1] == "#":
                grid[guard_pos[0]][guard_pos[1]] = "v"
    except:
        break

    if grid[guard_pos[0]][guard_pos[1]] == "^":
        guard_pos[0] -= 1
        grid[guard_pos[0]][guard_pos[1]] = grid[guard_pos[0] + 1][guard_pos[1]]
    elif grid[guard_pos[0]][guard_pos[1]] == "v":
        guard_pos[0] += 1
        grid[guard_pos[0]][guard_pos[1]] = grid[guard_pos[0] - 1][guard_pos[1]]
    elif grid[guard_pos[0]][guard_pos[1]] == "<":
        guard_pos[1] -= 1
        grid[guard_pos[0]][guard_pos[1]] = grid[guard_pos[0]][guard_pos[1] + 1]
    else:   # ">"
        guard_pos[1] += 1
        grid[guard_pos[0]][guard_pos[1]] = grid[guard_pos[0]][guard_pos[1] - 1]

sum = 0
for i in range(len(grid[0])):
    for j in range(len(grid)):
        if grid_visits[i][j] == "X":
            sum += 1
print("First Puzzle:", sum)


print("Second Puzzle:")
