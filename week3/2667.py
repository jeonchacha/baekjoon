# 2667 단지번호붙이기
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())
matrix = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):    
    visited[x][y] = True
    count = 1

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if not(0 <= nx < N and 0 <= ny < N):
            continue

        if not visited[nx][ny] and matrix[nx][ny] == 1:
            count += dfs(nx, ny)
    return count

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    count = 1
    while q:
        cx, cy = q.popleft()
        
        for dir in range(4):
            nx = cx + dx[dir]
            ny = cy + dy[dir]
        
            if not(0 <= nx < N and 0 <= ny < N):
                continue
        
            if not visited[nx][ny] and matrix[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1        
    return count

result = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and matrix[i][j] == 1:
            # result.append(dfs(i, j))
            result.append(bfs(i, j))

print(len(result))
for count in sorted(result):
    print(count)