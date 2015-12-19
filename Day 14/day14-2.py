# very inefficient, but works:
# for every second, recalculate the distance
# Then, once you have the distance, give points

def calc_points(time):
    for i in range(1, time+1):
        l = []
        for name in names:
            l += [calc_distance(name, i)]
        max_num = max(l)

        for el in range(len(names)):
            if l[el] == max_num:
                points[el] += 1

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

    names = list(reindeers.keys())
    points = [0 for x in names]
    calc_points(2503)

print(max(points))
