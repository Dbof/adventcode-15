# Approach: Build dictionary containing all rules of the input
# Then evaluate the dictionary starting with the requested key and using a recursive method

def build_dict(dic):
    with open('input.txt') as f:
        for line in f:
            inp, out = line.strip().split(' -> ')
            # output is key, input is value
            dic[out] = inp

def solve_dict(dic):
    # value of 'a' is requested
    return solve_entry(dic, 'a')

def solve_entry(dic, entry):
    # a few necessary checks
    if str(entry).isdigit():
        return int(entry)
    if str(dic[entry]).isdigit():
        return int(dic[entry])
    
    words = dic[entry].split()
    if len(words) == 1:
        if words[0].isdigit():
            return int(words[0])
        else:
            dic[entry] = solve_entry(dic, words[0])

    elif len(words) == 2:
        dic[entry] = ~ solve_entry(dic, words[1])

    else:
        if words[1] == 'AND':
            dic[entry] = solve_entry(dic, words[0]) & solve_entry(dic, words[2])

        elif words[1] == 'OR':
            dic[entry] =  solve_entry(dic, words[0]) | solve_entry(dic, words[2])
            
        elif words[1] == 'LSHIFT':
            dic[entry] = solve_entry(dic, words[0]) << int(words[2])

        else: # RSHIFT
            dic[entry] = solve_entry(dic, words[0]) >> int(words[2])

    return dic[entry]

# start with empty dict
wires = {}
build_dict(wires)
solution = solve_dict(wires)
print('Part 1:', solution)

# also solution 2
wires = {}
build_dict(wires)
wires['b'] = solution # "override wire b"
print('Part 2:', solve_dict(wires))
