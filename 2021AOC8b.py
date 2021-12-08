import os

## Part A, Set Up "Correct" number and letter relations, Define Functions

dir = os.path.dirname(__file__)
imported_data = open(dir + "\\2021AOC8 Display Digits Broken.txt","r")
data = []
output_num_list = []

for line in imported_data:
    data.append(line.strip('\n'))

cumulative_output_values = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}

correct_number_components = [
['a','b','c','e','f','g'],      #0 len(6) + (contains all letters in #1)
['c','f'],                      #1 identified by len(2)
['a','c','d','e','g'],          #2 len(5) + (has letter C)
['a','c','d','f','g'],          #3 len(5) + (contains all letters in #7)
['b','c','d','f'],              #4 identified by len(4)
['a','b','d','f','g'],          #5 len(5) + (NOT has letter C)
['a','b','d','e','f','g'],      #6 len(6) + (NOT match all letters in #1)
['a','c','f'],                  #7 identified by len(3)
['a','b','c','d','e','f','g'],  #8 identified by len(7)
['a','b','c','d','f','g']       #9 len(6) + (contains all letters in #4)
]

def compile_letter_number_relations(list):
    temp_dict = {'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[]}
    for index,num in enumerate(list):
        for component in num:
            temp_dict[component] += [index]
    return temp_dict

correct_letter_lookup = compile_letter_number_relations(correct_number_components)

def order_letters(str):
    list = []
    output = ""
    for letter in str:
        list.append(letter)
    list = sorted(list)
    output = output.join(list)
    return output

def all_exist(from_small, in_big):
    from_list = []
    in_list = []
    for x in range(0,len(from_small)):
        from_list.append(from_small[x])
    for y in range(0,len(in_big)):
        in_list.append(in_big[y])
    for a in from_list:
        if in_list.count(a) == 0:
            return False
    return True   

def decrypt_enigma_code(line):
    temp_list = []
    interpreter = ["","","","","","","","","",""]
    line_input_letters = line[:(line.index("|")-1):].split(" ")
    line_output_letters = line[(line.index("|")+2)::].split(" ")

    # Following sections must process in order of A, B, C, D blocks to derive all the right number+string pairings #

    # A #
    #1 identified by len(2)
    #4 identified by len(4)
    #7 identified by len(3)
    #8 identified by len(7)
    for i, i_each in enumerate(line_input_letters):
        if len(line_input_letters[i]) == 2:
            interpreter[1] = order_letters(i_each)
        elif len(line_input_letters[i]) == 3:
            interpreter[7] = order_letters(i_each)
        elif len(line_input_letters[i]) == 4:
            interpreter[4] = order_letters(i_each)
        elif len(line_input_letters[i]) == 7:
            interpreter[8] = order_letters(i_each)
    
    # B #
    #3 len(5) + (contains all letters in #7)
    #9 len(6) + (contains all letters in #4)
    #0 len(6) + (contains all letters in #1)
    #6 len(6) + (NOT match all letters in #1)
    for j, j_each in enumerate(line_input_letters):
        if len(line_input_letters[j]) == 5 and (all_exist(interpreter[7], j_each) == True):
            interpreter[3] = order_letters(j_each)
        elif len(line_input_letters[j]) == 6 and (all_exist(interpreter[4], j_each) == True):
            interpreter[9] = order_letters(j_each)
        elif len(line_input_letters[j]) == 6 and (all_exist(interpreter[1], j_each) == True):
            interpreter[0] = order_letters(j_each)
        elif len(line_input_letters[j]) == 6 and (all_exist(interpreter[1], j_each) == False):
            interpreter[6] = order_letters(j_each)
    
    # C #
    #  find letter C (exists in #1 + the letter which is NOT in #6)
    for letter in list(interpreter[1]):
        if list(interpreter[6]).count(letter) == 0:
            letter_C = letter

    # D #
    #2 len(5) + (has letter C)
    #5 len(5) + (NOT has letter C)
    for k, k_each in enumerate(line_input_letters):
        if len(line_input_letters[k]) == 5 and (all_exist(letter_C, k_each) == True) and order_letters(k_each) != interpreter[3]:
            interpreter[2] = order_letters(k_each)
        elif len(line_input_letters[k]) == 5 and (all_exist(letter_C, k_each) == False):
            interpreter[5] = order_letters(k_each)

    # Takes values from interpreter to calculate the numbers on the "output" values
    for item in line_output_letters:
        try: 
            if interpreter.index(order_letters(item)) == 0:
                temp_list.append("0")
            elif interpreter.index(order_letters(item)) == 1:
                temp_list.append("1")
            elif interpreter.index(order_letters(item)) == 2:
                temp_list.append("2")
            elif interpreter.index(order_letters(item)) == 3:
                temp_list.append("3")
            elif interpreter.index(order_letters(item)) == 4:
                temp_list.append("4")
            elif interpreter.index(order_letters(item)) == 5:
                temp_list.append("5")
            elif interpreter.index(order_letters(item)) == 6:
                temp_list.append("6")
            elif interpreter.index(order_letters(item)) == 7:
                temp_list.append("7")
            elif interpreter.index(order_letters(item)) == 8:
                temp_list.append("8")
            elif interpreter.index(order_letters(item)) == 9:
                temp_list.append("9")    
        except ValueError:
            pass
    return temp_list

## Part B, Execute

temp_num = ""

for line in data:
    returned_line = decrypt_enigma_code(line)
    temp_num = temp_num.join(returned_line)
    output_num_list.append(int(temp_num))
    temp_num = ""

print(sum(output_num_list))
