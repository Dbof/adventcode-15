import re

def count_vowels(string):
    vowels = re.findall('[aeiou]', string, re.IGNORECASE)
    return len(vowels)

def has_duplicate_char(string):
    for i in range(0, len(string)-1):
        if (string[i] == string[i+1]):
            return True
    return False

def contains_bad_parts(string):
    return any(sub in string for sub in ['ab', 'cd', 'pq', 'xy'])

def is_nice(string):
    return (count_vowels(string) >= 3 and has_duplicate_char(string) and not contains_bad_parts(string))

with open('input.txt', 'r') as f:
    count = 0
    for line in f:
        if is_nice(line):
            count += 1

print(count)
