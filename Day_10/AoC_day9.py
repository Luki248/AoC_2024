# Advent of Code
# Day 10
# https://adventofcode.com/2024/day/10

file = open("./Day_10/input.txt", "r")
input = file.readlines()

mountain = []
for line in input:
    line = line.rstrip("\n")
    temp = []
    for char in line:
        temp.append(int(char))
    mountain.append(temp)

def find_zeros():
    zeros = []
    for i in range(len(mountain)):
        for j in range(len(mountain[0])):
            if mountain[i][j] == 0:
                zeros.append([i, j])
    return zeros

zeros = find_zeros()

def find_next_trail(pos):
    if mountain[pos[0]][pos[0]] == 9:
        return pos
    
    trails = []
    if pos[0] < len(mountain) - 1:
        if mountain[pos[0] + 1][pos[1]] == mountain[pos[0]][pos[1]] + 1:
            trails.append([pos, find_next_trail([pos[0]+1, pos[1]])])
    if pos[0] > 1:
        if mountain[pos[0] - 1][pos[1]] == mountain[pos[0]][pos[1]] + 1:
            trails.append([pos, find_next_trail([pos[0]-1, pos[1]])])
    if pos[1] < len(mountain[0]) - 1:
        if mountain[pos[0]][pos[1] + 1] == mountain[pos[0]][pos[1]] + 1:
            trails.append([pos, find_next_trail([pos[0], pos[1]+1])])
    if pos[1] > 1:
        if mountain[pos[0]][pos[1] - 1] == mountain[pos[0]][pos[1]] + 1:
            trails.append([pos, find_next_trail([pos[0], pos[1]-1])])

    return trails

trails = []
for zero in zeros:
    trails.append(find_next_trail(zero))

print("First Puzzle:")


print("Second Puzzle:")
