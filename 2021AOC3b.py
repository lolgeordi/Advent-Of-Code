import os

binary_list = []
dir = os.path.dirname(__file__)

file = open(dir + "\\2021AOC3 Binary Values.txt", "r")

for item in file:
     binary_list.append(item.strip('\n'))

oxygen_list = binary_list
carbon_dioxide_list = binary_list

def most_frequent_bit(list, position):
    position_sums = [0,0]
    for i in list:
        if i[position] == '0':
            position_sums[0] += 1
        else:
            position_sums[1] += 1
    if position_sums[0] > position_sums[1]:
        return "0"
    elif position_sums[0] < position_sums[1]:
        return "1"
    else: 
        return "Equal"

def oxygen(list_a):
    temp_list = list_a
    most_freq = ""
    for x in range(0, 12): 
        most_freq = most_frequent_bit(temp_list, x)
        if len(temp_list) <=1:
            break
        elif most_freq == '0':
            temp_list = [z for z in temp_list if z[x] == "0"]
        elif most_freq == '1' or most_freq == 'Equal':
            temp_list = [z for z in temp_list if z[x] == "1"]
    return temp_list[0]

def carbon_dioxide(list_b):
    temp_list = list_b
    most_freq = ""
    for x in range(0, 12): 
        most_freq = most_frequent_bit(temp_list, x)
        if len(temp_list) <=1:
            break
        elif most_freq == '0':
            temp_list = [z for z in temp_list if z[x] == "1"]
        elif most_freq == '1' or most_freq == 'Equal':
            temp_list = [z for z in temp_list if z[x] == "0"]
    return temp_list[0]


print(f"Oxygen: {(oxygen(oxygen_list))}")
print(f"Oxygen Number: {int(oxygen(oxygen_list),2)}")
print(f"CO2: {(carbon_dioxide(carbon_dioxide_list))}")
print(f"CO2 Number: {int(carbon_dioxide(carbon_dioxide_list),2)}")
print(f"Life Support Rating: {int(carbon_dioxide(carbon_dioxide_list),2) * int(oxygen(oxygen_list),2)}")



# import os

# binary_list = [
# "00100",
# "11110",
# "10110",
# "10111",
# "10101",
# "01111",
# "00111",
# "11100",
# "10000",
# "11001",
# "00010",
# "01010"
# ]

# oxygen_list = binary_list
# carbon_dioxide_list = binary_list

# def most_frequent_bit(list, position):
#     position_sums = [0,0]
#     for i in list:
#         if i[position] == '0':
#             position_sums[0] += 1
#         else:
#             position_sums[1] += 1
#     if position_sums[0] > position_sums[1]:
#         return "0"
#     elif position_sums[0] < position_sums[1]:
#         return "1"
#     else: 
#         return "Equal"

# def oxygen(list_a):
#     temp_list = list_a
#     most_freq = ""
#     for x in range(0, 5): 
#         most_freq = most_frequent_bit(temp_list, x)
#         if len(temp_list) <=1:
#             break
#         elif most_freq == '0':
#             temp_list = [z for z in temp_list if z[x] == "0"]
#         elif most_freq == '1' or most_freq == 'Equal':
#             temp_list = [z for z in temp_list if z[x] == "1"]
#     return temp_list[0]

# def carbon_dioxide(list_b):
#     temp_list = list_b
#     most_freq = ""
#     for x in range(0, 5): 
#         most_freq = most_frequent_bit(temp_list, x)
#         if len(temp_list) <=1:
#             break
#         elif most_freq == '0':
#             temp_list = [z for z in temp_list if z[x] == "1"]
#         elif most_freq == '1' or most_freq == 'Equal':
#             temp_list = [z for z in temp_list if z[x] == "0"]
#     return temp_list[0]


# print(f"Oxygen: {(oxygen(oxygen_list))}")
# print(f"Oxygen Number: {int(oxygen(oxygen_list),2)}")
# print(f"CO2: {(carbon_dioxide(carbon_dioxide_list))}")
# print(f"CO2 Number: {int(carbon_dioxide(carbon_dioxide_list),2)}")
# print(f"Life Support Rating: {int(carbon_dioxide(carbon_dioxide_list),2) * int(oxygen(oxygen_list),2)}")

