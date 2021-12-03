import os

coordinates = [0,0]
directions = []
aim = 0

dir = os.path.dirname(__file__)

file = open(dir + "\\2021AOC2 Submarine Directions.txt", "r")

for line in file:
    directions.append(line.strip('\n'))

for index, item in enumerate(directions):
    directions[index] = item.split(' ')

for number in directions:
    number[1] = int(number[1])

for direction in directions: 
    if direction[0] == 'up':
        aim += (-1)*(direction[1])
    elif direction[0] == 'down':
        aim += (1)*(direction[1])
    elif direction[0] == 'forward':
        coordinates[0] += direction[1]
        coordinates[1] += (aim)*direction[1]

print('Coordinates are:')
print(coordinates)
print('Multiplied together =')
print(coordinates[0] * coordinates[1])
