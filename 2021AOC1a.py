DepthList = []
increases = 0
decreases = 0
nochanges = 0

File = open(r"C:\Users\Eric.Booth\Desktop\Depth List.txt")

for line in File:
    DepthList.append(int(line))

print("Total Measurements: " + str(len(DepthList)))

for count, item in enumerate(DepthList[0:2000]):
    if count == 0:
        previousitem = item
        next 
    elif item > previousitem:
        increases += 1
        previousitem = item
        next
    elif item < previousitem:
        decreases +=1
        previousitem = item
        next    
    else:
        nochanges +=1
        previousitem = item
        next    

print(
'''
In this list, from one value to the next there were:
{} increases
{} decreases
{} identical measurements
'''.format(increases, decreases, nochanges)

)