# Advent of Code
# Day 2
# https://adventofcode.com/2024/day/2


file = open("./Day_02/input.txt", "r")
input = file.readlines()

count_safe = 0
for line in input:
    line = line.strip("\n").split(" ")
    numbers = []
    for string in line:
        numbers.append(int(string))
    
    if numbers[0] < numbers[1]:
        increasing = True
    else:
        increasing = False

    is_safe = 1
    last = numbers[0]
    numbers.pop(0)
    for num in numbers:
        if not(abs(last - num) > 0 and abs(last - num) <= 3):
            is_safe = 0
        if increasing:
            if last > num:
                is_safe = 0
        else:
            if last < num:
                is_safe = 0
        last = num

    count_safe += is_safe
print("First Puzzle:", count_safe)


def test_for_safety(numbers):
    if numbers[0] < numbers[1]:
        increasing = True
    else:
        increasing = False

    is_safe = 1
    last = numbers[0]
    numbers.pop(0)
    for num in numbers:
        if not(abs(last - num) > 0 and abs(last - num) <= 3):
            is_safe = 0
        if increasing:
            if last > num:
                is_safe = 0
        else:
            if last < num:
                is_safe = 0
        last = num
    return is_safe

count_safe = 0
for line in input:
    line = line.strip("\n").split(" ")
    numbers = []
    for string in line:
        numbers.append(int(string))

    if not test_for_safety(numbers):
        is_safe = 0
        numbers_copy = numbers.copy()
        count_of_number_removes = 0
        for num in numbers:
            numbers = numbers_copy.copy()
            numbers.remove(num)
            if test_for_safety(numbers):
                is_safe += 1
                count_of_number_removes += 1
        print(count_of_number_removes)
        if is_safe == 0:
            count_safe += 1
    else:
        count_safe += 1

print("Second Puzzle:", count_safe)
