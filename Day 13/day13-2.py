import itertools
from collections import defaultdict

dic = defaultdict(dict)

def parse_line_to_dict(dic):
    # remove whitespace, dot and split the sentence
    text = line.strip()[:-1].split()
    # extract information
    who, gain, amount, nextto = text[0], text[2] == 'gain', int(text[3]), text[-1]
    if not gain:
        amount *= -1

    # save to dic
    dic[who][nextto] = amount

def add_myself_to_dict(dic):
    keys = list(dic.keys())
    for k in keys:
        dic['Me'][k] = 0
        dic[k]['Me'] = 0

def parse_happyness(dic, keys):
    result = 0
    key_len = len(keys)
    for i in range(0, key_len):
        k = keys[i]
        kn = keys[(i+1) % key_len]
        kprev = keys[i-1]

        ## print(k, "->", kn, '=', dic[k][kn])
        result += dic[k][kn]
        ## print(kprev, "->", k, '=', dic[k][kprev])
        result += dic[k][kprev]

    return result


with open('input.txt') as f:
    for line in f:
        parse_line_to_dict(dic)
    # adds 'Me' to the table
    add_myself_to_dict(dic)

    # create all permutations
    gen = itertools.permutations(dic.keys())

    max_happy = -10**100
    for x in gen:
        happyness = parse_happyness(dic, list(x))
        max_happy = max(max_happy, happyness)
    print(max_happy)
