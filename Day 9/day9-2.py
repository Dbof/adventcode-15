from collections import defaultdict

dic = defaultdict(dict)
cities = set()

def find_way(graph, cities, from_city, visited):
    if len(visited) == len(cities):
        return 0

    cost = -10**10 # arbitrary high number
    for to_city in cities:
        if from_city == to_city or to_city in visited:
            continue

        if to_city in graph[from_city]:
            vis = visited[:] + [to_city]
            cost = max(cost, graph[from_city][to_city] + find_way(graph, cities, to_city, vis))
    return cost

# read in file and save to dictionary
with open('input.txt') as f:
    for line in f:
        words = line.strip().split()
        fr, to, distance = words[0], words[2], int(words[-1])

        cities.add(fr)
        cities.add(to)
        dic[fr][to] = distance
        dic[to][fr] = distance 

print(max([find_way(dic, cities, city, [city]) for city in cities]))
