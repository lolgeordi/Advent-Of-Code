import os
import itertools

board = list([] for i in range(0,999))
for each in board:
    each += list(0 for j in range(0,999))

vectors = []
dir = os.path.dirname(__file__)
file = open(dir + "\\2021AOC5 Vectors.txt", "r")

def create_vector_list(file):
    output_list = []
    for item in file:
        output_list.append(item.strip('\n').replace(' -> ',',').split(','))
    return output_list

def add_to_board(list):
    global board
    if int(list[0]) > int(list[2]):
        x1 = int(list[2])
        y1 = int(list[3])
        x2 = int(list[0])
        y2 = int(list[1])
    elif int(list[1]) > int(list[3]):
        x1 = int(list[2])
        y1 = int(list[3])
        x2 = int(list[0])
        y2 = int(list[1])
    else:
        x1 = int(list[0])
        y1 = int(list[1])
        x2 = int(list[2])
        y2 = int(list[3])
    if x1 != x2 and y1 != y2:
        for z in range(0, abs(x1 - x2) + 1):
            if x1 > x2:
                x_mult = -1
            else:
                x_mult = 1
            if y1 > y2:
                y_mult = -1
            else:
                y_mult = 1
            board[x1 + (z * x_mult)][y1 + (z * y_mult)] += 1
    elif x1 == x2 and y1 == y2:
        board[x1][y1] += 1
    elif x1 == x2:
        for y in range(y1, (y2 + 1)):
            board[x1][y] += 1
    elif y1 == y2:
        for x in range(x1, (x2 + 1)):
            board[x][y1] += 1

def calc_overlap_points(array):
    global board
    x_len = len(array[:])
    y_len = len(array[0][:])
    sum = 0
    for x in range(0, x_len):
        for y in range(0, y_len):
            if board[x][y] != 1 and board[x][y] != 0:
                sum += 1
    return sum

vectors = create_vector_list(file)

for coordinates in vectors:
    add_to_board(coordinates)

print(calc_overlap_points(board))
