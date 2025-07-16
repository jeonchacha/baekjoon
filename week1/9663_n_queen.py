# n queen
# 같은 행, 열, 대각선에는 다른 퀸을 놓을 수 없음
# 같은 행에는 퀸을 놓지 않는다
# base case: i 가 n 이 되면 찾은것
# promising function: 같은 열이나 대각선에 놓이는 지를 확인
# 조건 1. 같은 열인지: col[i] == col[k] 라면 같은 열에 놓이게 되므로 non-promising
# 조건 2. 같은 대각선인지: col[i] - col[k] == abs(i - k)

# 백트래킹
# void checknode(node v)
# {
     # 자식노드
#     node u

    # 유망하다면
    # promising function 이 핵심    
#     if (promising(v))
#         if (v에 해답이 있으면)
#             해답 출력
#         else
#             for (모든 자식노드 u에 대하여)
                 # 재귀
#                checknode(u) 
# }

import sys

# def n_queens(i, col):
#     global count
#     n = len(col) - 1
#     if(promising(i, col)):
#         if i == n:
#             count += 1
#         else:
#             for j in range(1, n+1):
#                 col[i + 1] = j
#                 n_queens(i + 1, col)    

# def promising(i, col):
#     k = 1
#     flag = True
#     while(k < i and flag):
#         if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
#             flag = False
#         k += 1    
#     return flag

def n_queens(row):
    global count
    if row == N:
        count +=1
        return
    
    for col in range(N):
        if not col_used[col] and not diag1_used[row + col] and not diag2_used[row - col + N - 1]:
            col_used[col] = diag1_used[row + col] = diag2_used[row - col + N - 1] = True
            n_queens(row + 1)
            col_used[col] = diag1_used[row + col] = diag2_used[row - col + N - 1] = False 

N = int(sys.stdin.readline())
# col = [0] * (N + 1)
# n_queens(0, col)
count = 0
col_used = [False] * N
# 대각선 사용 여부 체크 배열 ( '/' 방향: row + col, '\' 방향: row - col + N - 1)
# '/' 방향은 (0, 3), (1, 2), (2, 1), (3, 0) 같이 이동 -> 이들 좌표의 공통점은 row + col 이 일정
# '\' 방향은 (0, 0), (1, 1), (2, 2), (3, 3) 같이 이동 -> 이들 좌표의 공통점은 row - col 이 일정
# -> row - col은 -(N-1)부터 +(N-1)까지의 값을 가짐 -> 음수 존재 -> 배열 인덱스는 음수 불가 -> 전체를 + N -1 만큼 shift
diag1_used = [False] * (2 * N - 1)
print(diag1_used)
diag2_used = [False] * (2 * N - 1)
n_queens(0)
print(count)