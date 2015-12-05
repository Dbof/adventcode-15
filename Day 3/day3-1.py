# set of houses where coordinates are saved as tuples
houses = set()
houses.add((0, 0)) # first house is always in set

santa = [0, 0] # santa's position

with open('input.txt') as f:
    while True:
        c = f.read(1)

        if c == '>':
            santa[0] += 1
        elif c == '<':
            santa[0] -= 1
        elif c == '^':
            santa[1] += 1
        elif c == 'v':
            santa[1] -= 1
        else:
            break

        houses.add(tuple(santa))
print(len(houses))
