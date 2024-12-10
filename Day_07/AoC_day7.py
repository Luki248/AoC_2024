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

def calc_res(nums):
    if len(nums) < 3:
        return nums[0] + nums[1], nums[0] * nums[1]
    else:
        ret = calc_res(nums[0:-1])
        calculations = []
        for res in ret:
            calculations.append(nums[-1] + res)
            calculations.append(nums[-1] * res)
        return calculations

is_eq_correct = []
for i in range(len(numbers)):
    number_of_results = pow(2, len(numbers[i]) - 1)
    eq_results = calc_res(numbers[i])

    is_equation_correct = False
    for res in eq_results:
        if res == results[i]:
            is_equation_correct = True
    is_eq_correct.append(is_equation_correct)

sum = 0
for i in range(len(is_eq_correct)):
    if is_eq_correct[i]:
        sum += results[i]
print("First Puzzle:", sum)


def calc_res2(nums):
    if len(nums) < 3:
        return nums[0] + nums[1], nums[0] * nums[1], int(str(nums[0]) + str(nums[1]))
    else:
        ret = calc_res2(nums[0:-1])
        calculations = []
        for res in ret:
            calculations.append(nums[-1] + res)
            calculations.append(nums[-1] * res)
            calculations.append(int(str(res) + str(nums[-1])))
        return calculations

is_eq_correct2 = []
for i in range(len(numbers)):
    number_of_results = pow(3, len(numbers[i]) - 1)
    eq_results = calc_res2(numbers[i])

    is_equation_correct = False
    for res in eq_results:
        if res == results[i]:
            is_equation_correct = True
    is_eq_correct2.append(is_equation_correct)

sum2 = 0
for i in range(len(is_eq_correct2)):
    if is_eq_correct2[i]:
        sum2 += results[i]
print("Second Puzzle:", sum2)
