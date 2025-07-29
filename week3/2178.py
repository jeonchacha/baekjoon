# 2178 미로 탐색
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(N)]
dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0))
    visited = set()
    visited.add((0, 0))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not(0 <= nx < N and 0 <= ny < M):
                continue

            if graph[nx][ny] == 1 and (nx, ny) not in visited:
                q.append((nx, ny))
                visited.add((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    return graph[N-1][M-1]

print(bfs())