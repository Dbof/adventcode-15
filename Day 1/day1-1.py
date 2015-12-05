counter = 0
with open('input.txt') as f:
    while True:
        c = f.read(1)

        if c == '(':
            counter += 1
        elif c == ')':
            counter -= 1
        else:
            break
    print(counter)
