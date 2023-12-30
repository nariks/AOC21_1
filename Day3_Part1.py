
with open("input_day3.txt") as file:
    lines = [list(line.rstrip()) for line in file]

binary_report, vertical_totals = [], []

for line in lines:
    binary_report.append([int(digit, base = 2) for digit in line])

digit_count = len(binary_report[0])
line_count = len(binary_report)

for i in range(digit_count):
    vertical_totals.append(sum([line[i] for line in binary_report]))

msb, lsb = "", ""

for total in vertical_totals:
    if total > line_count // 2:
        msb += "1"
        lsb += "0"
    else:
        msb += "0"
        lsb += "1"

gamma = int(msb, base = 2)
epsilon = int(lsb, base = 2)

print(gamma * epsilon)







