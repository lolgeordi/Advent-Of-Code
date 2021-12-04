import os

binary_list = []
position_sums = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
gamma = ""
epsilon = ""

dir = os.path.dirname(__file__)

file = open(dir + "\\2021AOC3 Binary Values.txt", "r")

for item in file:
    binary_list.append(item.strip('\n'))

for i in binary_list:
    for y, j in enumerate(i):
        if j == '0':
            position_sums[y][0] += 1
        else:
            position_sums[y][1] += 1

for pair in position_sums:
    if pair[0] > pair[1]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(f"Gamma: {int(gamma, 2)}")
print(f"Epsilon: {int(epsilon, 2)}")
print(f"Multiplied: {int(epsilon, 2) * int(gamma, 2)}")