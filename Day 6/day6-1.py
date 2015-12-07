## uses a set to determine if light is on. If it is, the coordinates are present in the set.
## This solution is probably slower than creating a 1000x1000 grid and looping through it...

def set_grid(coord1, coord2):
    global grid
    print("Set", coord1, coord2)
    xs, ys = coord1
    xe, ye = coord2
    l = [(x,y) for x in range(xs, xe+1) for y in range(ys, ye+1)]
    grid.union(l)

def unset_grid(coord1, coord2):
    global grid
    print("Unset", coord1, coord2)
    xs, ys = coord1
    xe, ye = coord2
    l = [(x,y) for x in range(xs, xe+1) for y in range(ys, ye+1)]
    grid.difference(l)

def toggle_grid(coord1, coord2):
    global grid
    print("Toggle", coord1, coord2)
    xs, ys = coord1
    xe, ye = coord2
    l = []
    for x in range(xs, xe+1):
        for y in range(ys, ye+1):
            l += [(x, y)]

    grid = grid.symmetric_difference(l)

with open('input.txt') as f:
    grid = set()
    for line in f:
        command = line.split() # split at spaces
        if command[0] == 'toggle':
            c1 = list(map(int, command[1].split(',')))
            c2 = list(map(int, command[3].split(',')))
            toggle_grid(c1, c2)
        else:
            c1 = list(map(int, command[2].split(',')))
            c2 = list(map(int, command[4].split(',')))
            if command[1] == 'on': 
               set_grid(c1, c2)
            else:
               unset_grid(c1, c2)
    print(len(grid))
