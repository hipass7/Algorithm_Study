N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
from itertools import combinations
chickens = []
houses = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chickens.append((i, j))
        elif city[i][j] == 1:
            houses.append((i, j))

def get_distance(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

def get_chicken_distance(chickens):
    total_distance = 0
    for house in houses:
        min_distance = float('inf')
        for chicken in chickens:
            distance = get_distance(house, chicken)
            min_distance = min(min_distance, distance)
        total_distance += min_distance
    return total_distance

min_distance = float('inf')
for selected_chickens in combinations(chickens, M):
    distance = get_chicken_distance(selected_chickens)
    min_distance = min(min_distance, distance)
print(min_distance)

