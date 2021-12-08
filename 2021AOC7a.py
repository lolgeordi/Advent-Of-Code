import os
import collections

dir = os.path.dirname(__file__)
import_data = open(dir + "\\2021AOC7 Crab Submarines.txt")
initial_list = []
crab_dict = {}
lowest_fuel = 999999999999999999999999999
lowest_position = 0

for item in import_data:
    initial_list += item.strip("/n").split(",")

for a in range(0, len(initial_list)):
    initial_list[a] = int(initial_list[a])

crab_dict = collections.Counter(initial_list)
crab_range = sorted(set(crab_dict))
range_min = crab_range[0]
range_max = crab_range[len(crab_range)-1]

def crab_calc(dictionary, integer):
    fuel_cost = 0
    for crab in crab_range:
        fuel_cost += (abs(crab - integer) * dictionary[crab])
    return fuel_cost

for position in range(range_min, range_max + 1):
    current_fuel = crab_calc(crab_dict, position) 
    if current_fuel < lowest_fuel:
        lowest_fuel = current_fuel
        lowest_position = position

print(f"Lowest fuel consumption: {lowest_fuel}")
print(f"Target position for optimal fuel consumption: {lowest_position}")
