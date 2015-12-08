# first calculate original number, then encode and count again

with open('input.txt') as f:
    total_code, total_new = 0, 0
    for line in f:
        line = line.strip()
        total_code += len(line)

        # encode line
        newstr = line.replace('\\', '\\\\').replace('"', '\\\"')
        total_new += len(newstr) + 2 # remember 2 " around string

print(total_new - total_code)
