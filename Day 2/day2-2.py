
def bow_length(w, h, l):
    return w*h*l

def ribbon_length(w, h, l):
    x, y = sorted([w, h, l])[0:2]
    return 2*x + 2*y

def calc_ribbon(w, h, l):
    return ribbon_length(w, h, l) + bow_length(w, h, l)

with open('input.txt') as f:
    total = 0
    for line in f:
        w, h, l = map(int, line.split('x'))
        total += calc_ribbon(w, h, l)

    print(total)
