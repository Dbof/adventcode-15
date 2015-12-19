# define a min depth
min_depth = 100

# this could be made faster with sorted list
def find_combinations():
    # This time the containers are sorted in descending order
    # The first 'match' will be with the least number of containers
    con = list(reversed(sorted(containers)))
    print(con)
    return find(liters, con, 1)

# very simple backtracking algorithm
def find(curr_value, con, depth):
    global min_depth
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
            # but only count solutions with the min depth
            if depth <= min_depth:
                count += 1
                min_depth = min(min_depth, depth)
        else:
            # might have multiple solutions
            count += find(remaining, copy, depth+1)
    return count

liters = 150
containers = []
with open('input.txt') as f:
    for line in f:
        containers += [int(line)]

print(find_combinations())
