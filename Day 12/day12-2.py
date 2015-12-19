import json

def parse_list(l):
    result = 0
    for i in l:
        if type(i) is dict:
            result += parse_dict(i)
        elif type(i) is list:
            result += parse_list(i)
        elif type(i) is int:
            result += i
        else: ## string
            pass
    return result

def parse_dict(js):
    result = 0
    for k, v in js.items():
        # ignore any object containing 'red'
        if k == 'red' or v == 'red':
            return 0

        if type(v) is dict:
            result += parse_dict(v)

        elif type(v) is list:
            result += parse_list(v)

        elif type(v) is int:
            result += v

        else: ## string
            pass
    return result

with open('input.txt') as f:
    js = json.load(f)
    result = parse_dict(js)
    print(result)
