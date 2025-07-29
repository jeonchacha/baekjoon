# 11725 트리의 부모 찾기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input().strip())
adj_list = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int,input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)
parent = [0] * (N + 1)
start = 1

def dfs(node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)

    for neighbor in adj_list[node]:
        if neighbor not in visited:
            parent[neighbor] = node
            dfs(neighbor, visited)

dfs(start)

for ans in parent[2:]:
    print(ans)