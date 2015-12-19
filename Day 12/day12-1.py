# Slightly cheating here: 
# Find the numbers by going through the 
# text and look for numbers
import re

with open('input.txt') as f:
    text = f.read()
    l = re.findall(r'-?\d+', text)
    l = [int(i) for i in l]
print(sum(l))
