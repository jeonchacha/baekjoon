# 1707 이분 그래프
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
K = int(input().strip())

for _ in range(K):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    colors = [0] * (V + 1)
    visited = [False] * (V + 1)

    def dfs(node, color):

        visited[node] = True
        colors[node] = color

        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                if not dfs(neighbor, 3 - color):
                    return False
            elif colors[neighbor] == colors[node]:
                    return False
        return True

    is_bipartite = True
    for i in range(1, V+1):
         if not visited[i]:
              if not dfs(i, 1):
                   is_bipartite = False
                   break

    print('YES' if is_bipartite else 'NO') 
