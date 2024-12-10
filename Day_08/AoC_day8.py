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

print("First Puzzle:")

print("Second Puzzle:")
