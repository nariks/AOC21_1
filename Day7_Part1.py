with open("input_day7.txt") as file:
    crab_positions = file.readline().strip().split(",")

crab_positions = [int(position) for position in crab_positions]
fuel_cost = []

def calculate_fuel(location, crab_position):
    n = abs(location - crab_position)
    return  (n * (n+1)) / 2


for crab_position in range(max(crab_positions)):
    fuel_cost.append(sum([calculate_fuel(location, crab_position) for location in crab_positions]))

print(min(fuel_cost))
