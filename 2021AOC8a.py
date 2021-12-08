import os

## Part A, Set Up "Correct" number and letter relations, Define Functions

dir = os.path.dirname(__file__)
imported_data = open(dir + "\\2021AOC8 Display Digits Broken.txt","r")
data = []

for line in imported_data:
    data.append(line.strip('\n'))

cumulative_output_values = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

correct_number_components = [
['a','b','c','e','f','g'],
['c','f'],
['a','c','d','e','g'],
['a','c','d','f','g'],
['b','c','d','f'],
['a','b','d','f','g'],
['a','b','d','e','f','g'],
['a','c','f'],
['a','b','c','d','e','f','g'],
['a','b','c','d','f','g']
]

def compile_letter_number_relations(list):
    temp_dict = {'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[]}
    for index,num in enumerate(list):
        for component in num:
            temp_dict[component] += [index]
    return temp_dict

correct_letter_lookup = compile_letter_number_relations(correct_number_components)

def decrypt_enigma_code(line):
    temp_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    interpreter = ["","","","","","","","","",""]
    line_input_letters = line[:(line.index("|")-1):].split(" ")
    line_output_letters = line[(line.index("|")+2)::].split(" ")
    for i, each in enumerate(line_output_letters):
        if len(line_output_letters[i]) == 2:
            temp_dict[1] += 1
        elif len(line_output_letters[i]) == 3:
            temp_dict[7] += 1
        elif len(line_output_letters[i]) == 4:
            temp_dict[4] += 1
        elif len(line_output_letters[i]) == 7:
            temp_dict[8] += 1
    return temp_dict

## Part B, Execute

for line in data:
    returned_line = decrypt_enigma_code(line)
    for item in returned_line:
        cumulative_output_values[item] += returned_line[item]

print(f"The total of each letter in all the output was as follows: {cumulative_output_values}")
print(f"The total sum: {sum(cumulative_output_values.values())}")
