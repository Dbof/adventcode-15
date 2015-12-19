# calculate distance with simple math

def calc_distance(name, time):
    speed, fly, rest = reindeers[name]
    remaining = time
    resting = False

    distance = 0
    while (remaining > 0):
        if resting:
            remaining -= rest
            resting = False
        else:
            if remaining >= fly:
                distance += fly*speed
                remaining -= fly
                resting = True
            else:
                distance += remaining*speed
                remaining = 0
    return distance


reindeers = {}
dists = []
with open('input.txt') as f:
    for line in f:
        data = line.strip().split()
        name, speed, time, rest = data[0], int(data[3]), int(data[6]), int(data[-2])

        reindeers[name] = (speed, time, rest)
        dists += [calc_distance(name, 2503)]

print(max(dists))
