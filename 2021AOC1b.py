import os

DepthList = []
increases = 0
decreases = 0
nochanges = 0
checkCurrent = None
checkPastOne = None
checkPastTwo = None
checkPastThree = None

File = open(os.path.expanduser('~\\Desktop\\2021AOC1 Depth List.txt'), "r")

for line in File:
    DepthList.append(int(line))

for item in DepthList[0:2000]:
    checkPastThree = checkPastTwo
    checkPastTwo = checkPastOne
    checkPastOne = checkCurrent
    checkCurrent = item
    if (checkPastThree == None) or (checkPastTwo == None) or (checkPastOne == None) or (checkCurrent == None):
        next 
    elif (checkCurrent + checkPastOne + checkPastTwo) > (checkPastOne + checkPastTwo + checkPastThree):
        increases += 1
        next
    elif (checkCurrent + checkPastOne + checkPastTwo) < (checkPastOne + checkPastTwo + checkPastThree):
        decreases +=1
        next    
    else:
        nochanges +=1
        next    

print(
'''
In this list of past three measurement rolling averages, from one rolling average to the next there were:
{} increases
{} decreases
{} identical measurements
'''.format(increases, decreases, nochanges)

)