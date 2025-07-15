import sys
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

def n_queens(i, col):
    n = len(col) - 1
    if(promising(i, col)):
        if i == n:
            print(col[1: n+1])
        else:
            for j in range(1, n+1):
                col[i + 1] = j
                n_queens(i + 1, col)    

def promising(i, col):
    k = 1
    flag = True
    while(k < i and flag):
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
            flag = False
        k += 1    
    return flag

n = 4
col = [0] * (n + 1)
n_queens(0, col)