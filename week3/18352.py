# 18352 특정 거리의 도시 찾기
import sys
from collections import deque
input = sys.stdin.readline
# N 도시의 개수, M 도로의 개수, K 거리 정보, X 출발 도시
N, M, K, X = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
dist = [-1] * len(adj_list)
dist[X] = 0

def bfs():
    q = deque([X])
    visited = [False] * len(adj_list)
    visited[X] = True
    while q:
        node = q.popleft()
        
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                dist[neighbor] = dist[node] + 1
                visited[neighbor] = True
                q.append(neighbor)
bfs()

found = False
for city in range(1, N+1):
    if dist[city] == K:
        print(city)
        found = True
if not found:
    print(-1)