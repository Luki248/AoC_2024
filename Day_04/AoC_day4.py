# Advent of Code
# Day 4
# https://adventofcode.com/2024/day/4

file = open("./Day_04/input.txt", "r")
input = file.readlines()

grid = []
for line in input:
    grid.append(line.rstrip("\n"))

find = "XMAS"
find2 = "SAMX"

counts = 0
# horizontally
for line in grid:
    counts += line.count(find)
    counts += line.count(find2)

# transpose the grid
grid_inv = []
for _ in range(len(grid)):
    grid_inv.append(len(grid)*([0]))

for i in range(len(grid)):
    for j in range(len(grid[0])):
        grid_inv[len(grid) - i - 1][len(grid[0]) - j - 1] = grid[j][i]
    string = ""
    for chr in grid_inv[len(grid) - i - 1]:
        string += chr
    grid_inv[len(grid) - i - 1] = string

# vertically
for line in grid_inv:
    counts += line.count(find)
    counts += line.count(find2)

# diagonally
for i in range(len(grid) - 3):
    for j in range(len(grid) - 3):
        if grid[i][j] == find[0]:
            if grid[i+1][j+1] == find[1]:
                if grid[i+2][j+2] == find[2]:
                    if grid[i+3][j+3] == find[3]:
                        counts += 1
for i in range(len(grid) - 3):
    for j in range(len(grid) - 3):
        if grid[i][j] == find2[0]:
            if grid[i+1][j+1] == find2[1]:
                if grid[i+2][j+2] == find2[2]:
                    if grid[i+3][j+3] == find2[3]:
                        counts += 1
for i in range(len(grid_inv) - 3):
    for j in range(len(grid_inv) - 3):
        if grid_inv[i][j] == find[0]:
            if grid_inv[i+1][j+1] == find[1]:
                if grid_inv[i+2][j+2] == find[2]:
                    if grid_inv[i+3][j+3] == find[3]:
                        counts += 1
for i in range(len(grid_inv) - 3):
    for j in range(len(grid_inv) - 3):
        if grid_inv[i][j] == find2[0]:
            if grid_inv[i+1][j+1] == find2[1]:
                if grid_inv[i+2][j+2] == find2[2]:
                    if grid_inv[i+3][j+3] == find2[3]:
                        counts += 1

print("First Puzzle:", counts)

print("Second Puzzle:")
