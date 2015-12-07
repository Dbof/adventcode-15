## use 2d array as grid

def set_val(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            grid[x][y] += 1

def unset_val(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            grid[x][y] -= 1 if grid[x][y] > 0 else 0

def toggle_val(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            grid[x][y] += 2

with open('input.txt') as f:
    grid = [[0 for x in range(1000)] for x in range(1000)]
    for line in f:
        command = line.split() # split at spaces
        if command[0] == 'toggle':
            c1 = list(map(int, command[1].split(',')))
            c2 = list(map(int, command[3].split(',')))
            toggle_val(c1, c2)
        else:
            c1 = list(map(int, command[2].split(',')))
            c2 = list(map(int, command[4].split(',')))
            if command[1] == 'on': 
               set_val(c1, c2)
            else:
               unset_val(c1, c2)
    # sum all rows, then the results together
    print(sum(map(sum, grid)))
