# This solution reads the file byte for byte, so it is a little slower,
# but is requires less memory

counter = 0
with open('input.txt') as f:
    while True:
        c = f.read(1) # read byte for byte

        if c == '(':
            counter += 1
        elif c == ')':
            counter -= 1
        else:
            break
    print(counter)
