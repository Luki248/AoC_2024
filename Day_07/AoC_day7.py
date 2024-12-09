# Advent of Code
# Day 7
# https://adventofcode.com/2024/day/7

file = open("./Day_07/input.txt", "r")
input = file.readlines()

results = []
numbers = []
for line in input:
    line = line.rstrip("\n")
    res, nums = line.split(":")
    results.append(int(res))
    nums = nums.strip(" ").split(" ")
    nums_int = []
    for num in nums:
        nums_int.append(int(num))
    numbers.append(nums_int)

def calc_res(nums, operator):
    if len(nums) < 3:
        if operator == "+":
            return nums[0] + nums[1]
        else:
            return nums[0] * nums[1]
    else:
        if operator == "+":
            return nums[0] + calc_res(nums[1:], "+")
        else:
            return nums[0] * calc_res(nums[1:], "+")

print(calc_res(numbers[1], "+"))
print("First Puzzle:")


print("Second Puzzle:")
