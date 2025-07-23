# 3190 뱀
import sys
from collections import deque
input = sys.stdin.readline
N = int(input().strip())  # 보드 크기
K = int(input().strip())  # 사과 개수
board = [[0] * N for _ in range(N)]     # 0은 빈칸, 1은 사과
for _ in range(K):  # 사과 세팅
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1
# 방향전환 정보 저장
L = int(input().strip())
turns = {}
for _ in range(L):
    t, c = input().split()
    turns[int(t)] = c

snake = deque()
snake.append((0, 0))    # 시작위치

# 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0
# direction = 0 → 오른쪽
# direction = 1 → 아래
# direction = 2 → 왼쪽
# direction = 3 → 위

time = 0
x, y = 0, 0     # 뱀 머리의 현재 위치
while True:
    time += 1
    # 다음에 머리가 갈 좌표
    # 현재 방향에 따라 머리를 앞으로 한 칸 이동
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 벽에 부딪히는 조건 : 범위 벗어남
    if not (0 <= nx < N and 0 <= ny < N):
        break
    # 몸에 부딪힘: snake 안에 머리 좌표가 이미 있음
    if (nx, ny) in snake:
        break

    # 머리 앞으로 이동
    snake.appendleft((nx, ny))

    if board[nx][ny] == 1:  # 사과 있으면    
        board[nx][ny] = 0   # 사과 먹고
        # 꼬리 안 자름 (길이 증가)
    else:
        snake.pop()     # 사과 없으면 꼬리 자름
    
    # 회전 시점이면
    if time in turns:
        if turns[time] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

    # 오른쪽 90도 회전: 시계 방향 → +1
    # 왼쪽 90도 회전: 반시계 방향 → -1
    # 방향은 4개니까 mod 4 연산
    # direction = (direction + 1) % 4  # 오른쪽
    # direction = (direction - 1) % 4  # 왼쪽

    # 다음 루프를 위해 현재 머리 위치 갱신
    x, y = nx, ny
    
print(time)