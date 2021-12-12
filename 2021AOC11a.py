import os

dir = os.path.dirname(__file__)
data = open(dir + "\\2021AOC11 Octopus Flashes.txt")
octopus_lists = [[],[],[],[],[],[],[],[],[],[]]
user_input = int(input("Provide integer - how many steps to process? "))
flash_count = 0

for index, line in enumerate(data):
    for character in line:
        character = character.strip()
        if character != '':
            octopus_lists[index].append([int(character),0,"None"])

def flash_refresh():
    global octopus_lists
    global total_flashes
    for x, item in enumerate(octopus_lists):
        for y, each in enumerate(item):
            if each[2] == "None" and each[1] > 9:
                octopus_lists[x][y][2] = "Flash"
            elif each[2] == "Flash":
                octopus_lists[x][y][2] = "Already"

def lookup_flash():
    global octopus_lists
    for item in octopus_lists:
        for each in item:
            if each[2] == "Flash":
                return True
    return False                

def flash_check(position_x, position_y):
    global octopus_lists
    new_value = octopus_lists[position_x][position_y][1]
    check_list = [
        [position_x - 1, position_y - 1], 
        [position_x - 1, position_y + 0], 
        [position_x - 1, position_y + 1], 
        [position_x - 0, position_y + 1], 
        [position_x - 0, position_y - 1], 
        [position_x + 1, position_y - 1], 
        [position_x + 1, position_y + 0], 
        [position_x + 1, position_y + 1]
        ]
    for index, each in enumerate(check_list):
        if each[0] in range(0,len(octopus_lists)) and each[1] in range(0,len(octopus_lists[index])):
            if octopus_lists[each[0]][each[1]][2] == "Flash":
                octopus_lists[position_x][position_y][1] += 1


def step():
    global octopus_lists
    global flash_count
    had_flash = False
    temp_flash_track = False
    flash_results = []
    # First, the energy level of each octopus increases by 1.
    for x, xrow in enumerate(octopus_lists):
        for y, yspecimen in enumerate(xrow):
            octopus_lists[x][y][1] = octopus_lists[x][y][0] + 1

    # Then, any octopus with an energy level greater than 9 flashes. 
    # This increases the energy level of all adjacent octopuses by 1, 
    # including octopuses that are diagonally adjacent. If this causes 
    # an octopus to have an energy level greater than 9, it also flashes. 
    # This process continues as long as new octopuses keep having their 
    # energy level increased beyond 9. (An octopus can only flash at most once per step.)
    
    flash_refresh()

    while lookup_flash() == True:
        for a, arow in enumerate(octopus_lists):
            for b, bspecimen in enumerate(arow):
                flash_check(a, b)
        flash_refresh()

    # Finally, any octopus that flashed during this step has its energy 
    # level set to 0, as it used all of its energy to flash.
    for i, irow in enumerate(octopus_lists):
        for j, jspecimen in enumerate(irow): 
            if octopus_lists[i][j][1] > 9:
                octopus_lists[i][j][0] = 0
                flash_count += 1
            else:
                octopus_lists[i][j][0] = octopus_lists[i][j][1]

for x in range (1, user_input + 1):
    step()
    for x, item in enumerate(octopus_lists):
        for y, each in enumerate(item):
            octopus_lists[x][y][2] = "None"
    
print(octopus_lists)
print(f"Total Flash Count Was: {flash_count}")
