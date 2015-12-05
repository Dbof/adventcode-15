
def surface(w, h, l):
    return 2*w*h + 2*h*l + 2*l*w

def extra_surface(w, h, l):
    x, y = sorted([w, h, l])[0:2]
    return x*y

def calc_paper(w, h, l):
    return surface(w, h, l) + extra_surface(w, h, l)

with open('input.txt') as f:
    total = 0
    for line in f:
        w, h, l = map(int, line.split('x'))
        total += calc_paper(w, h, l)

    print(total)
