from functools import reduce
import itertools

def calc_score(ratios):
    props = [0 for g in range(4)]

    # first add all attribute values of all ingredients together
    for k,v in ingredients.items():
        for attr_i in range(4):
            # attributes
            props[attr_i] += ratios[k]*v[attr_i]

    # set attributes < 0 to 0
    for attr_i in range(4):
        if props[attr_i] < 0:
            props[attr_i] = 0

    # multiply all attribute scores
    score = reduce(lambda x,y: x*y, props)    
    return score

# create permutations of possible ratios of ingredients
def create_permutations(in_list):
    # 4 ingredients, each ranging from 0 to 100
    for ratio in itertools.product(range(101), repeat=len(in_list)):
        if sum(ratio) == 100: # 100%
            yield ratio

def find_best():
    # create generator
    gen_perm = create_permutations(ingredient_list)

    best_score = 0
    for p in gen_perm:
        ratio = {}
        # assign ratios to ingredients list (order has to be constant)
        for i, val in enumerate(ingredient_list):
            ratio[val] = p[i]

        # calculate the score
        score = calc_score(ratio)
        if score > best_score:
            best_score = score
            print("Current max:", score)

ingredients = {}
with open('input.txt') as f:
    for line in f:
        d = line.strip().replace(',', '').replace(':', '').split()

        name, cap, dur, fla, tex, cal = d[0], int(d[2]), int(d[4]), int(d[6]), int(d[8]), int(d[-1])
        ingredients[name] = (cap, dur, fla, tex, cal)
        print(name, ingredients[name])

ingredient_list = list(ingredients.keys())
find_best()
