# Advent of Code
# Day 8
# https://adventofcode.com/2024/day/8

file = open("./Day_08/input.txt", "r")
input = file.readlines()

grid = []
for line in input:
    line = line.rstrip("\n")
    lin = []
    for i in line:
        lin.append(i)
    grid.append(lin)

antennas = []
for i in range(len(grid[0])):
    for j in range(len(grid)):
        if grid[i][j] != ".":
            antennas.append([grid[i][j], i, j])

total_antinodes = 0
for ant1 in antennas:
    print(i)

    for ant2 in antennas:
        if ant1 == ant2:
            continue
        if ant1[0] == ant2[0]:
            delta_y = abs(ant1[1] - ant2[1])
            if ant1[1] > ant2[1]:
                antinode_y1 = ant1[1] + delta_y
                antinode_y2 = ant2[1] - delta_y
            else:
                antinode_y2 = ant1[1] + delta_y
                antinode_y1 = ant2[1] - delta_y
            delta_x = abs(ant1[2] - ant2[2])
            if ant1[2] > ant2[2]:
                antinode_x1 = ant1[2] + delta_x
                antinode_x2 = ant2[2] - delta_x
            else:
                antinode_x1 = ant1[2] + delta_x
                antinode_x2 = ant2[2] - delta_x

            if antinode_x1 >= 0 and antinode_x1 < len(grid[0]):
                if antinode_y1 >= 0 and antinode_y1 < len(grid):
                    total_antinodes += 1
            if antinode_x2 >= 0 and antinode_x2 < len(grid[0]):
                if antinode_y2 >= 0 and antinode_y2 < len(grid):
                    total_antinodes += 1

print("First Puzzle:")

print("Second Puzzle:")
