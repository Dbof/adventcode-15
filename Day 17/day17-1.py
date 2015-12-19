# this could be made faster with sorted list
def find_combinations():
    con = list(containers)
    print(con)
    return find(liters, con)

# very simple backtracking algorithm
def find(curr_value, con):
    copy = con[:] # create new copy
    count = 0
    for c in con:
        copy.remove(c)
        remaining = curr_value - c
        if remaining < 0:
            # no solution
            pass
        elif remaining == 0:
            # found solution
            count += 1
        else:
            # might have multiple solutions
            count += find(remaining, copy)
    return count

liters = 150
containers = []
with open('input.txt') as f:
    for line in f:
        containers += [int(line)]
print(find_combinations())
