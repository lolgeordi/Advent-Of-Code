import os

days = int(input("How many days after initial state do you want to run?: "))
fish_list = []

dir = os.path.dirname(__file__)
imported_data = open(dir + "\\2021AOC6 Lanternfish.txt", "r")

for data in imported_data:
    fish_list += data.strip('\n').split(",")

for a in range(len(fish_list)):
    fish_list[a] = int(fish_list[a])

def next_day(list):
    zero_count = list.count(0)
    new_fish_list = list
    for x in range(0, len(new_fish_list)):
        if new_fish_list[x] == 0:
            new_fish_list[x] = 6
        else:
            new_fish_list[x] = new_fish_list[x] - 1
    for count in range(0,zero_count):
        new_fish_list.append(8)
    return new_fish_list

for day in range(0, days):
    fish_list = next_day(fish_list)
    print(f"Count of fish as of day {day}: {len(fish_list)}")
