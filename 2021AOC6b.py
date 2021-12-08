import os

days = int(input("How many days after initial state do you want to run?: "))
fish_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
fish_sum = 0
initial_list = []

dir = os.path.dirname(__file__)
imported_data = open(dir + "\\2021AOC6 Lanternfish.txt", "r")

for data in imported_data:
    initial_list += data.strip('\n').split(",")

for a in range(len(initial_list)):
    initial_list[a] = int(initial_list[a])
    fish_dict[initial_list[a]] += 1

def next_day(dict):
    zero = dict[0]
    one = dict[1]
    two = dict[2]
    three = dict[3]
    four = dict[4]
    five = dict[5]
    six = dict[6]
    seven = dict[7]
    eight = dict[8]
    dict[0] = one
    dict[1] = two
    dict[2] = three
    dict[3] = four
    dict[4] = five
    dict[5] = six
    dict[6] = zero + seven
    dict[7] = eight
    dict[8] = zero
    return dict

for day in range(0, days):
    fish_dict = next_day(fish_dict)
    fish_sum = sum(fish_dict.values())
    print(f"Count of fish as of day {day + 1}: {fish_sum}")
