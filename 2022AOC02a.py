import os

dir = os.path.dirname(__file__)

file = open(dir + "\\2022AOC02 puzzle input.txt", "r")
turns = []
total_score = 0

for line in file:
    turns.append((line[0],line[2]))

def calc_score(abc, xyz):
    if abc == "A":
        player_one = "Rock"
    elif abc == "B":
        player_one = "Paper"
    elif abc == "C":
        player_one = "Scissors"
    if xyz == "X": 
        player_two = "Rock"
    elif xyz == "Y":
        player_two = "Paper"
    elif xyz == "Z":
        player_two = "Scissors"

    if player_two == "Rock" and player_one == "Rock": 
        return int(3+1)
    if player_two == "Rock" and player_one == "Paper": 
        return int(0+1)
    if player_two == "Rock" and player_one == "Scissors": 
        return int(6+1)
    if player_two == "Paper" and player_one == "Rock": 
        return int(6+2)
    if player_two == "Paper" and player_one == "Paper": 
        return int(3+2)
    if player_two == "Paper" and player_one == "Scissors": 
        return int(0+2)
    if player_two == "Scissors" and player_one == "Rock": 
        return int(0+3)
    if player_two == "Scissors" and player_one == "Paper": 
        return int(6+3)
    if player_two == "Scissors" and player_one == "Scissors": 
        return int(3+3)

for every in turns:
    turn_score = print(calc_score(every[0],every[1]))
    turn_score = calc_score(every[0],every[1])
    total_score += turn_score

print(total_score)