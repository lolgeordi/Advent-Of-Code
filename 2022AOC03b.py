import os
from collections import Counter

dir = os.path.dirname(__file__)

file = open(dir + "\\2022AOC03 puzzle input.txt", "r")

total = 0
counter = 1
temp_list = []
final_list = []

def priority_lookup(letter):
    letters_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return (letters_list.find(letter) + 1)

for line in file:
    cleaned_line = line.strip('\n')
    if counter == 3:
        set_format = set(cleaned_line)
        list_format = list(set_format)
        for each in list_format:
            temp_list.append(each)
        c = Counter(temp_list)
        dictionary = dict(c)
        for letter, count in dictionary.items():
            if count == 3:
                final_list.append(letter)
        counter = 1  
        temp_list = []   

    else:
        set_format = set(cleaned_line)
        list_format = list(set_format)
        for each in list_format:
            temp_list.append(each)    
        counter += 1

for item in final_list:
    total += priority_lookup(item)

print(total)
