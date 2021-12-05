import os

dir = os.path.dirname(__file__)
text_file = open(dir + "\\2021AOC4 Bingo.txt", "r")
num_list = text_file.readline().strip("\n").split(",")
boards = {}
last_winning_num = None
last_boards = []
current_boards = []
previous_boards = []

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
    bingo_list = set(bingo_list)
    return list(bingo_list)

def winning_board_calc(key):
    unmarked_total = 0
    for i, row in enumerate(boards[key]):
        for j, column in enumerate(row):
            if boards[key][i][j][1] != "X":
                unmarked_total += int(boards[key][i][j][0])
    return unmarked_total

def unique(list):
    list_set = set(list)
    return list(list_set)

# actual processing begins below #
create_boards(text_file)

for num in num_list:
    mark_boards(num)
    current_boards = check_boards(boards)
    if len(current_boards) == 100:
        last_winning_num = num
        break
    previous_boards = current_boards

last_boards = [x for x in current_boards if x not in previous_boards]

print("We have our last boards!")
print(f"Last winning number: {last_winning_num}")

print(previous_boards)
print(current_boards)
print(num_list)

for last in last_boards:
    print(f"Board #: {last}")
    print(f"Remaining total: {winning_board_calc(last)}")
    print(f"Multiplied by winning number: {winning_board_calc(last) * int(last_winning_num)}")

#6526 answer is TOO HIGH