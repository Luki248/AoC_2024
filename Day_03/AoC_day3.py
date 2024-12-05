# Advent of Code
# Day 3
# https://adventofcode.com/2024/day/3

import re

file = open("./Day_03/input.txt", "r")
input = file.readlines()
all_lines_together = input[0] + input[1] + input[2] + input[3] + input[4] + input[5]

s = re.findall("mul\(\d+,\d+\)", all_lines_together)
sum = 0
for mul in s:
    numbers = re.findall("\d+", mul)
    sum += int(numbers[0]) * int(numbers[1])
print("First Puzzle:", sum)

s = re.findall("mul\(\d+,\d+\)|don't\(\)|do\(\)", all_lines_together)
sum = 0
do_mul = True
for mul in s:
    if mul == "do()":
        do_mul = True
    elif mul == "don't()":
        do_mul = False
    elif do_mul:
        numbers = re.findall("\d+", mul)
        sum += int(numbers[0]) * int(numbers[1])
print("Second Puzzle:", sum)
