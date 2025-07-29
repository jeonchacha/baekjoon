# 14888 연산자 끼워넣기
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_val = -float('inf')
min_val = float('inf')

def dfs(idx, result, plus, minus, mul, div):
    global max_val, min_val

    if idx == N:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return
    
    num = A[idx]

    if plus > 0:
        dfs(idx + 1, result + num, plus - 1, minus, mul, div)
    if minus > 0:
        dfs(idx + 1, result - num, plus, minus - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, result * num, plus, minus, mul - 1, div)
    if div > 0:
        if result < 0:
            dfs(idx + 1, -(-result // num), plus, minus, mul, div - 1)
        else: 
            dfs(idx + 1, result // num, plus, minus, mul, div - 1)
            
dfs(1 ,A[0], plus, minus, mul, div)
print(max_val)
print(min_val)