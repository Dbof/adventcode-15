def has_repeated_pair(string):
    for i in range(0, len(string)-1):
        pair = string[i:i+2]
        if pair in string[i+2:]:
            return True
    return False

def has_repeated_letter(string):
    for i in range(0, len(string)-2):
        if string[i] == string[i+2]:
            return True
    return False

def is_nice(string):
    return (has_repeated_pair(string) and has_repeated_letter(string))

with open('input.txt', 'r') as f:
    count = 0
    for line in f:
        if is_nice(line):
            print(line)
            count += 1

print(count)
