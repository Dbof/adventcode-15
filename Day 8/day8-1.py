with open('input.txt') as f:
    total_code, total_data = 0, 0
    for line in f:
        line = line.strip()
        total_code += len(line)
        
        # simply evaluate the line in python
        res = eval(line)
        total_data += len(res)

print(total_code - total_data)
