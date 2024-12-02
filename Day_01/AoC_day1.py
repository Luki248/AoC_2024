# Advent of Code
# Day 1
# https://adventofcode.com/2024/day/1


file = open("./Day_01/input.txt", "r")
input = file.readlines()

numbers1 = []
numbers2 = []
numbers3 = []
numbers4 = []
for line in input:
    line = line.strip("\n").split(" ")
    numbers1.append(int(line[0]))
    numbers2.append(int(line[3]))
    numbers3.append(int(line[0]))
    numbers4.append(int(line[3]))

total_distance = 0
for i in range(len(numbers1)):
    min1 = min(numbers1)
    numbers1.remove(min1)
    min2 = min(numbers2)
    numbers2.remove(min2)
    total_distance += abs(min1 - min2)
print("First Puzzle:", total_distance)

similarity_score = 0
for num in numbers3:
    count = numbers4.count(num)
    score = count * num
    similarity_score += score
print("Second Puzzle:", similarity_score)
