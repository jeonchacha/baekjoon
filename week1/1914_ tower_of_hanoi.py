# 2^n - 1
# base case: 재귀 호출을 더 이상 나누지 않고 바로 답을 내릴 수 있는 가장 작은(종료) 케이스
# n == 1 -> 출발 기둥(A)에서 목표 기둥(C)로 옮기면 끝 
# recursive case: 문제를 더 작은 동일한 문제로 분할하여 결국 base case에 도달하도록 설계된 부분
# n > 1 -> 1. 맨 아래(가장 큰) 원판을 제외한 n-1개를 A -> B(보조기둥)로 이동
#          2. 가장 큰 원판 하나를 A -> C로 이동
#          3. 보조 기둥 B에 쌓인 n-1개를 B -> C로 이동
# 맨 아래 원판 제외하고는 위에 몇개가 있던지 하나의 덩어리로 봐야함

# 입력 매개변수
# n: 옮길 원판의 개수
# source: 출발 기둥
# auxiliary: 보조 기둥
# target: 목표 기둥

# pseudocode
# funtion HANOI(n, source, auxiliary, target)
#   # base case
#   if n == 1:
#       move disk from source to target     # 2. 가장 큰 원판 하나를 A -> C로 이동
#       return
#
#   # recursive case
#   HANOI(n-1, source, target, auxiliary)   # 1. 맨 아래(가장 큰) 원판을 제외한 n-1개를 A -> B(보조기둥)로 이동
#   move disk from source to target         # 2. 가장 큰 원판 하나를 A -> C로 이동
#   HANOI(n-1, auxiliary, source, target)   # 3. 보조 기둥 B에 쌓인 n-1개를 B -> C로 이동

# def hanoi(n, source, auxiliary, target, depth):
#     indent = '  ' * depth
#     print(f'{indent}enter hanoi({n}, {source} -> {target})')

#     # base case
#     if n == 1:
#         print(f'{indent}    move disk 1: {source} -> {target}')
#         print(f'{indent}exit hanoi({n}, {source} -> {target})')
#         return
#     # recursive case
#     hanoi(n-1, source, target, auxiliary, depth+1)
#     print(f'{indent}    move disk {n}: {source} -> {target}')
#     hanoi(n-1, auxiliary, source, target, depth+1)
#     print(f'{indent}exit hanoi({n}, {source} -> {target})')

# n = 3 
# hanoi(n, 'A', 'B', 'C', 0)

import sys

n = int(sys.stdin.readline().strip())

def hanoi(n, start, middle, end):
    if n == 1:
        print(start, end)
        return
    
    hanoi(n-1, start, end, middle)
    print(start, end)
    hanoi(n-1, middle, start, end)
# **: 제곱
print(2**n - 1)

if n <= 20:
    hanoi(n, 1, 2, 3)