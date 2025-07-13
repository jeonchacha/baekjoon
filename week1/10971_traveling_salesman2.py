import sys
import itertools

n = int(sys.stdin.readline())
w = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

INF = float('inf')
best_cost = INF
start_city = 0

rest_cities = list(range(1,n))

# n개의 요소에 대한 순열의 경우의 수는 n!
for perm in itertools.permutations(rest_cities):
    current_cost = 0
    prev = start_city

    for city in perm:
        if w[prev][city] == 0:
            break

        current_cost += w[prev][city]
        
        if current_cost >= best_cost:
            break
        prev = city
    else:
         if w[prev][start_city] == 0:
            continue
         
         current_cost += w[prev][start_city]
         if current_cost < best_cost:
             best_cost = current_cost   

print(best_cost)