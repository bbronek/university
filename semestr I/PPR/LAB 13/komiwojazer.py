import sys
from itertools import permutations

def dist(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def generate_paths(cities_idx):
    start_city = cities_idx[0]
    for perm in permutations(cities_idx[1:]):
        yield (start_city,) + perm + (start_city,)

def path_distatnce(path,cities):
    distance = 0
    for city_1,city_2 in zip(path[:-1],path[1:]):
        distance += dist(cities[city_1],cities[city_2])
    return distance

def generate_all_paths(cities):
    cities_list = list(range(len(cities)))
    for path in generate_paths(cities_list):
        yield path_distatnce(path,cities)

def main():
    cities = []
    for line in sys.stdin:
        cities.append([int(num) for num in line.split()])
    min_distance = min(generate_all_paths(cities))
    print(f'{min_distance:.1f}')

if __name__ == '__main__':
    main()