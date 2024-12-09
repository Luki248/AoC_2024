# Advent of Code
# Day 5
# https://adventofcode.com/2024/day/5

import math

file = open("./Day_05/input.txt", "r")
input = file.readlines()

rules = []
tests = []
for line in input:
    line = line.rstrip("\n")
    if line.count("|") == 1:
        numbers = line.split("|")
        rules.append([int(numbers[0]), int(numbers[1])])
    if line.count(",") >= 1:
        numbers = line.split(",")
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        tests.append(numbers)

def check_tests(test):
    for rule in rules:
        if test.count(rule[0]) == 1 and test.count(rule[1]) == 1:
            found_nr_1 = False
            found_nr_2 = False
            for i in range(len(test)):
                if test[i] == rule[0]:
                    found_nr_1 = True
                if test[i] == rule[1]:
                    found_nr_2 = True
                if found_nr_2 and (not found_nr_1):
                    return False
    return True

test_results = []
for test in tests:
    test_results.append(check_tests(test))

sum = 0
for i in range(len(tests)):
    if test_results[i]:
        length = len(tests[i])
        sum += tests[i][math.floor(length / 2)]
print("First Puzzle:", sum)


def check_tests2(test):
    wrong_rules = []
    is_wrong = False
    for rule in rules:
        if test.count(rule[0]) == 1 and test.count(rule[1]) == 1:
            found_nr_1 = False
            found_nr_2 = False
            for i in range(len(test)):
                if test[i] == rule[0]:
                    found_nr_1 = True
                if test[i] == rule[1]:
                    found_nr_2 = True
                if found_nr_2 and (not found_nr_1):
                    if wrong_rules.count(rule) < 1:
                        wrong_rules.append(rule)
                    is_wrong = True
    return [not is_wrong, wrong_rules]

test_results = []
wrong_rules = []
for test in tests:
    res, wrong = check_tests2(test)
    test_results.append(res)
    wrong_rules.append(wrong)

print(test_results)
print(wrong_rules)

sum2 = 0
for i in range(len(tests)):
    test = tests[i]
    if test_results[i] == False:
        middle_index = math.floor(len(test) / 2)

        if len(wrong_rules[i]) > 1:
            pass
        else:
            rule_wrong_rules = wrong_rules[i][0]
            if (test[middle_index] == rule_wrong_rules[0]) or (test[middle_index] == rule_wrong_rules[1]):
                print(test)
                if test[middle_index] == rule_wrong_rules[0]:
                    sum2 += rule_wrong_rules[1]
                if test[middle_index] == rule_wrong_rules[1]:
                    sum2 += rule_wrong_rules[0]
            else:
                sum2 += test[middle_index]
print("Second Puzzle:", sum2)
