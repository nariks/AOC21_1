with open("input_day6.txt") as file:
    fish_states = file.readline().strip().split(",")

fish_status = { 0: [int(state) for state in fish_states]}

def update_states(days):
    if days  > 0:
        for day in fish_status:
            for i in range(len(fish_status[day])):
                if fish_status[day][i] == 0:
                    fish_status[day][i] = 6
                    fish_status[len(fish_status) - 1].append(8)
                else:
                    fish_status[day][i] -= 1
        update_states(days - 1)


update_states(80)
sum = 0

for day in fish_status:
    sum += len(fish_status[day])

print(sum)


