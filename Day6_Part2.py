with open("input_day6.txt") as file:
    fish_states = file.readline().strip().split(",")

spawn_states = [0] * 9

for fish_state in fish_states:
    spawn_states[int(fish_state)] += 1

def update_states(days):
    if days > 0:
        new_spawns = spawn_states[0]
        spawn_states.insert(len(spawn_states) - 1, spawn_states.pop(0))
        spawn_states[6] += new_spawns
        update_states(days - 1)

update_states(256)
print(sum(spawn_states))





