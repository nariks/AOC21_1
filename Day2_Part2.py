with open("input_day2.txt") as file:
    lines = [line.rstrip().split() for line in file]

sub_position = {"horizontal": 0, "depth": 0, "aim": 0}

for line in lines:
    if line[0] == "forward":
        sub_position["horizontal"] += int(line[1])
        sub_position["depth"] += int(line[1]) * sub_position["aim"]
    elif line[0] == "down":
        sub_position["aim"] += int(line[1])
    elif line[0] == "up":
        sub_position["aim"] -= int(line[1])

print(sub_position["horizontal"] * sub_position["depth"])