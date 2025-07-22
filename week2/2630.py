# 백준 2630 색종이 만들기

import sys
input = sys.stdin.readline
# 하얀색(0), 파란색(1) 색종이의 개수 출력
# 전체 종이가 모두 같은 색이 아니면 n/2
# 잘라진 종이가 모두 같은 색으로 칠해져 있거나, 하나의 정사각형 칸이 되어 자를 수 없을 때까지 반복
# base case = n == 1

def cut_paper(x, y, N):
    global white
    global blue

    if N == 1:
        if paper[x][y] == 0:
            white += 1
        else:
            blue += 1
        return
    
    prev = paper[x][y]
    for i in range(N):
        for j in range(N):
            if prev != paper[x+ i][y + j]:
                half = N // 2
                cut_paper(x, y, half)
                cut_paper(x, y + half, half)
                cut_paper(x + half, y, half)
                cut_paper(x + half, y + half, half)
                return # 이미 다른 색을 발견했기 때문에 더 이상 현재 함수를 진행하면 안된다. 

    if prev == 0:
        white += 1
    elif prev == 1:
        blue += 1              

N = int(input().strip())
paper = [list(map(int,input().split())) for _ in range(N)]

white = 0
blue = 0
cut_paper(0, 0, N)
print(white)
print(blue)    
