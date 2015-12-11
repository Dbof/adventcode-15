alphabet = list('abcdefghijklmnopqrstuvwxyz')
not_allowed = list('iol')
alphabet = [x for x in alphabet if x not in not_allowed]
PASS_LENGTH= 8

def check_length(p):
    return len(p) == PASS_LENGTH

def check_increasing(p):
    # requirement 1
    for i in range(PASS_LENGTH-2):
        char = p[i]
        index = alphabet.index(char)
        if index >= len(alphabet)-2:
            continue

        if p[i+1] == alphabet[index+1] and p[i+2] == alphabet[index+2]:
            return True
    return False

def check_is_allowed(p):
    # requirement 2
    return not set(not_allowed).issubset(p)

def check_pairs(p):
    pairs = []
    for i in range(PASS_LENGTH-1):
        if p[i] == p[i+1] and p[i] not in pairs:
            pairs += p[i]
    return len(pairs) >= 2

def is_valid(password):
    return check_length(password) and check_increasing(password) and check_is_allowed(password) and check_pairs(password)

def increment(password, index):
    """
    Recursive approach to increment a password
    """

    index = index % len(password) # wrap-around
    aindex = alphabet.index(password[index])
    # assign the next letter in the alphabet (with wrap-around)
    password[index] = alphabet[(aindex+1) % len(alphabet)]

    if password[index] == alphabet[0] and index != 0:
        return increment(password, index-1)
    return password


inp = 'hepxcrrq'
while not is_valid(inp):
    inp = increment(list(inp), -1)
print(''.join(inp))

# part 2
inp = increment(list(inp), -1)
while not is_valid(inp):
    inp = increment(list(inp), -1)
print(''.join(inp))
