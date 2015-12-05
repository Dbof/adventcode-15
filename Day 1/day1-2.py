counter, position = 0, 0
with open('input.txt') as f:
    while True:
        c = f.read(1)
        position += 1

        if c == '(':
            counter += 1
        elif c == ')':
            counter -= 1
        else:
            break
        
        if counter == -1:
            break
print(position)
