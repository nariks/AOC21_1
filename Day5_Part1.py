with open("input_day5.txt") as file:
    coordinates = [line.strip().split(" -> ") for line in file]

rows, cols = 1000, 1000
layout = [[0 for row in range(rows)] for col in range (cols)]

for coordinate in coordinates:
    x1, y1 = coordinate[0].strip().split(",")
    x2, y2 = coordinate[1].strip().split(",")
    x1, x2 = int(x1), int(x2)
    y1, y2 = int(y1), int(y2)

    if y1 == y2:
        x_range = range(x1, x2 + 1) if x2 > x1 else range(x2, x1 + 1)
        for x in x_range:
            layout[y1][x] += 1
    elif x1 == x2:
        y_range = range(y1, y2 + 1) if y2 > y1 else range(y2, y1 + 1)
        for y in y_range:
            layout[y][x1] += 1

danger_points = 0

for i in range(rows):
    for j in range(cols):
        if layout[i][j] >= 2:
            danger_points += 1

print(danger_points)


