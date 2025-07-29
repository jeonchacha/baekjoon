# 2606 바이러스
import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
adj_list = [[] for _ in range(N + 1)]
start = 1
for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

def bfs(adj_list, start):
    q = deque([start])
    visited = [False] * len(adj_list)
    visited[start] = True

    while q:
        node = q.popleft()
        
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True    # 큐에 넣을 때 방문 처리
                q.append(neighbor)
    
    return sum(visited) - 1

print(bfs(adj_list, start))