import os

dir = os.path.dirname(__file__)
text_file = open(dir + "\\2021AOC4 Bingo.txt", "r")
num_list = text_file.readline().strip("\n").split(",")
boards = {}
winning_num = None

def create_boards(file):
    global boards
    key = "0"
    for line in file:
        if line == '\n':
            key = str(int(key) + 1)
            boards[key] = []
        else:
            new = line.strip('\n')
            boards[key].append(
            new.split(" ")
            )
    for board in boards.keys():
        for i, row in enumerate(boards[board]):
            for j, column in enumerate(row):
                if boards[board][i][j] == '':
                    boards[board][i].remove('')
    for board in boards.keys():
        for k, row2 in enumerate(boards[board]):
            for l, column2 in enumerate(row2):
                boards[board][k][l] = [column2, ""]

def mark_boards(number):
    global boards
    for board in boards.keys():
        for i, row in enumerate(boards[board]):
            for j, column in enumerate(row):
                if boards[board][i][j][0] == number:
                    boards[board][i][j][1] = "X"

def check_boards(dictionary):
    bingo_list = []
    for board in boards.keys():
        marker = 0
        for i, row in enumerate(boards[board]):
            for j, column in enumerate(row):
                if boards[board][i][j][1] == "X":
                    marker += 1
                    if marker == 5:
                        bingo_list.append(board)
                else:
                    marker = 0
                    break 
        for col in range(0,5):
            for k, ro in enumerate(boards[board]):
                if boards[board][k][col][1] == "X": 
                    marker += 1
                    if marker == 5:
                        bingo_list.append(board)
                else:
                    marker = 0
                    break                  
    return bingo_list

def winning_board_calc(key):
    unmarked_total = 0
    for i, row in enumerate(boards[key]):
        for j, column in enumerate(row):
            if boards[key][i][j][1] != "X":
                unmarked_total += int(boards[key][i][j][0])
    return unmarked_total

# actual processing begins below #
create_boards(text_file)

for num in num_list:
    mark_boards(num)
    current_boards = check_boards(boards)
    if current_boards != []:
        winning_num = int(num)
        break
        

print(f"These board numbers had Bingo first: {current_boards}")
for each in current_boards:
    calc_remaining_nums = winning_board_calc(each)
    print(f"Sum of unmarked numbers for board #{int(each)}: {calc_remaining_nums}")
    print(f"Winning Number: {winning_num}")
    print(f"Multiplied Together: {winning_num * calc_remaining_nums}")

