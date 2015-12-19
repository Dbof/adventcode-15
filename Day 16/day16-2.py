ticker = {'children': 3, 'cats': '>7', 'samoyeds':2, 'pomeranians': '<3', 'akitas': 0, 'vizslas': 0, 'goldfish': '<5', 'trees': '>3', 'cars': 2, 'perfumes': 1}

# changed search pattern for ticker
def search_correct():
    for nr, sue in enumerate(sue_list):
        nr = nr+1
        match = 0
        for k,v in ticker.items():
            if k in sue:
                if type(v) is str:
                    num = int(v[1])
                    if v[0] == '<' and sue[k] < num or v[0] == '>' and sue[k] > num:
                        match += 1
                elif v == sue[k]:
                    # attribute match!
                    match += 1

        if match == len(sue.keys()):
            return (nr, sue)


sue_list = []
with open('input.txt') as f:
    for line in f:
        # strip out everything unnecessary
        data = line.strip().replace(',', '').replace(':', '').split()
        nr = int(data[1])

        # len of data is always even
        attrs = data[2:]
        # create dictionary for every aunt
        for i in range(0, len(attrs), 2):
            name, val = attrs[i], int(attrs[i+1])
            sue_list += [{}]
            sue_list[nr-1][name] = val

print(search_correct())
