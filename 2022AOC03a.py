import os
from collections import Counter

dir = os.path.dirname(__file__)

file = open(dir + "\\2022AOC03 puzzle input.txt", "r")

total = 0

def priority_lookup(letter):
    letters_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return (letters_list.find(letter) + 1)

def half_len(line):
    cleaned_line = line.strip('\n')
    return len(cleaned_line)/2

def dup_check(string_a, string_b):
    for a in string_a:
        for b in string_b:
            if a == b:
                return a

for line in file:
    first_half = line[0:int(half_len(line))]
    second_half = line[int(half_len(line)):int(len(line))]
    total += priority_lookup(dup_check(first_half, second_half))

print(total)