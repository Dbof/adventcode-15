from copy import deepcopy # for copying 2d array

# calculate the next state for a given light
def next_state(lights, y, x, state):
    neighbours = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            try:
                if j == i and i == 0:
                    continue
                row = y+i
                col = x+j
                if row < 0 or col < 0:
                    continue

                if lights[row][col]:
                    neighbours += 1
            except IndexError:
                continue

    if state:
        return neighbours == 2 or neighbours == 3
    else:
        return neighbours == 3


# update step for all lights
# a new copy is created every time to preserve state
def update_lights(lights):
    new_lights = deepcopy(lights)
    for y, row in enumerate(lights):
        for x, state in enumerate(row):
            new_lights[y][x] = next_state(lights, y, x, state)
    return new_lights

# return all lights that are 'on'
def count_lights_on(lights):
    return sum([l.count(True) for l in lights])

lights = []
with open('input.txt') as f:
    row = 0
    for line in f:
        data = line.strip()
        # create row
        lights += [[]]

        # read char for char
        for c in data:
            lights[row] += [True] if c == '#' else [False]        
        row += 1

# backup lights for later
backup = deepcopy(lights)

# part 1 #
print('Starting with:', count_lights_on(lights))
for i in range(1, 100+1):
    lights = update_lights(lights)

print(count_lights_on(lights))


# part 2 #
lights = backup
lights[0][0] = lights[0][99] = lights[99][0] = lights[99][99] = True
print('Starting with:', count_lights_on(lights))
for i in range(1, 100+1):
    lights = update_lights(lights)
    # set corners manually
    lights[0][0] = lights[0][99] = lights[99][0] = lights[99][99] = True

print(count_lights_on(lights))
