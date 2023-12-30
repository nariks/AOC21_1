with open("input_day8.txt") as file:
    signals = [line.strip().split("|")[1].split() for line in file]

#print(signals)
unique_digits = [2, 3, 4, 7]
count = 0

for signal in signals:
    for digit in signal:
        #print (digit, len(digit))
        if len(digit) in unique_digits:
            count += 1

print(count)

