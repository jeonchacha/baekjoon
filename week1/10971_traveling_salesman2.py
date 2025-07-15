import sys
import itertools

# n = int(sys.stdin.readline())
# w = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
n = 4
w = [
    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 13, 0, 12],
    [8, 8, 9, 0]
]
# 무한대로 초기화
INF = float('inf')
# 최솟값을 찾을 변수라 초기화를 무한대로
best_cost = INF
start_city = 0

rest_cities = list(range(1,n))

# n개의 요소에 대한 순열의 경우의 수는 n!
for perm in itertools.permutations(rest_cities):
    print(perm)
    current_cost = 0
    prev = start_city

    for city in perm:
        # 길이 없는 경우
        if w[prev][city] == 0:
            break

        current_cost += w[prev][city]
        
        # 더이상 이 경로는 최적이 될 수 없으므로 중단
        if current_cost >= best_cost:
            break
        prev = city
    else:
         # for-else: 중간에 break 안당한 경우만 여기로

         # 마지막 -> 출발 도시로 돌아올 때
         if w[prev][start_city] == 0:
            continue
         
         current_cost += w[prev][start_city]
         if current_cost < best_cost:
             best_cost = current_cost   

print(best_cost)