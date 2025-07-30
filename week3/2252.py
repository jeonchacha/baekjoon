# 2252 줄 세우기
import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    in_degree[v] += 1

def topological_bfs(adj_list, in_degree):
    result = []
    q = deque([node for node in range(1, len(in_degree)) if in_degree[node] == 0])

    while q:
        node = q.popleft()
        result.append(node)

        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)
                        
    if len(result) != N:
        return -1
    return result

result = topological_bfs(adj_list, in_degree)
if result == -1:
    print(-1)
else:
    ##### 리스트를 언팩해서 공백 구분으로 출력 #####
    print(*result)