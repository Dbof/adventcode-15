def count_sequence(seq):
    actual = seq[0]
    count = 0
    result = []
    for c in seq:
        if c == actual:
            count += 1
        else:
            result += [[actual, count]]
            count = 1

        actual = c
    result += [[actual, count]]
    return result


def look_and_say(text):
    array = count_sequence(text)
    result = ''
    for a in array:
        result += str(a[1]) + str(a[0])
    return result

out = '1113122113'
print(out)
for i in range(40):
    out = look_and_say(out)
print('10-1:', len(out))

# second challenge
out = '1113122113'
for i in range(50):
    out = look_and_say(out)
print('10-2:', len(out))
