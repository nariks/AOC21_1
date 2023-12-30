
with open("input_day3.txt") as file:
    lines = [list(line.rstrip()) for line in file]

binary_report = []
for line in lines:
    binary_report.append([int(digit, base = 2) for digit in line])

def calculate_rating(binary_report, mcb_flag):       # mcb_flag is True for Oxygen rating and False for CO2 rating
    rating_report = binary_report

    for i in range(len(binary_report[0])):
        vertical_total = sum([line[i] for line in rating_report])
        count = len(rating_report)

        if vertical_total == count / 2 or vertical_total > count // 2:
            common_bit = int(True and mcb_flag)
        else:
            common_bit = int(not(True and mcb_flag))

        if count > 1:
            rating_report = [line for line in rating_report if common_bit == line[i]]

    return rating_report


oxygen_rating = calculate_rating(binary_report, True)
co2_rating = calculate_rating(binary_report, False )

oxygen = int(("".join([str(digit) for digit in oxygen_rating[0]])), base = 2)
co2 = int(("".join([str(digit) for digit in co2_rating[0]])), base = 2)

print(oxygen * co2)










