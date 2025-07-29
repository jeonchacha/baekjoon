# 11724 연결 요소의 개수
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

def dfs(node, visited):
    visited.add(node)
    for neighbor in adj_list[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)

count = 0
visited = set()
for i in range(1, N + 1):
    if i not in visited:
        dfs(i, visited)
        count += 1

print(count)