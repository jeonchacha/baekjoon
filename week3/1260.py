# 1260 DFS와 BFS
import sys
from collections import deque
sys.setrecursionlimit(10**6)

def dfs(adj, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    result = [node] 

    for neighbor in adj[node]:
        if neighbor not in visited:
            result += dfs(adj, neighbor, visited)
    return result

def bfs(adj, start):
    result = []
    q = deque([start])
    visited = [False] * len(adj)
    visited[start] = True

    while q:
        node = q.popleft()
        result.append(node)

        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True # 큐에 넣을 때 방문처리
                q.append(neighbor)

    return result

input = sys.stdin.readline

N, M, start = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)  # 무방향 그래프
# 각 정점의 인접 노드 오름차순 정렬
for neighbors in adj:
    neighbors.sort()

dfs_result = dfs(adj, start)
bfs_result = bfs(adj, start)
print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))