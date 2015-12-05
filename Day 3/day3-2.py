# set of houses where coordinates are saved as tuples
houses = set()
houses.add((0, 0)) # first house is always in set

santa = [0, 0] # santa's position
robo = [0, 0] # robo santa's position
santasturn = True

with open('input.txt') as f:
    while True:
        c = f.read(1)
        if santasturn:
            character = santa
        else:
            character = robo
        
        if c == '>':
            character[0] += 1
        elif c == '<':
            character[0] -= 1
        elif c == '^':
            character[1] += 1
        elif c == 'v':
            character[1] -= 1
        else:
            break

        # alternate turn
        santasturn = not santasturn

        houses.add(tuple(character))
print(len(houses))
