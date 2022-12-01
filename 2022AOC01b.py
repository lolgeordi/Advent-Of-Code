import os

largestnum_one = 0
largestnum_two = 0
largestnum_three = 0
tempnum = 0
currentnum = 0
dir = os.path.dirname(__file__)

file = open(dir + "\\2022AOC01 puzzle input.txt", "r")

for line in file:
    templine = line.strip('\n')
    if templine == "":
        if tempnum > largestnum_one:
            largestnum_three = largestnum_two
            largestnum_two = largestnum_one
            largestnum_one = tempnum
        elif tempnum > largestnum_two:
            largestnum_three = largestnum_two
            largestnum_two = tempnum
        elif tempnum > largestnum_three:
            largestnum_three = tempnum
        tempnum = 0
    else:
        currentnum = int(templine)
        tempnum += currentnum

print(largestnum_one + largestnum_two + largestnum_three)