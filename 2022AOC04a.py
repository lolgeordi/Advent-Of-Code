import os

dir = os.path.dirname(__file__)

file = open(dir + "\\2022AOC04 puzzle input.txt", "r")

running_count = 0

def split_line_comma(string):
    split_list = string.strip('\n').split(",")
    return split_list

def split_line_dash(string):
    new_list = [0,0]
    split_list = string.split("-")
    for x, item in enumerate(split_list):
        new_list[x] = int(item)
    return new_list

for line in file: 
    split_line = split_line_comma(line)
    part_a = split_line_dash(split_line[0])
    part_b = split_line_dash(split_line[1])
    if (part_a[0] >= part_b[0] and part_a[1] <= part_b[1]) or (part_a[0] <= part_b[0] and part_a[1] >= part_b[1]):
        running_count += 1

print(running_count)