# 백준 1629번 곱셈
import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())

def mod_pow(A, B, C):
    if B == 0:
        return 1
    
    temp = mod_pow(A, B // 2, C)
    temp = (temp * temp) % C
    if B % 2 == 1:
        temp = (temp * A) % C
    return temp

print(mod_pow(A, B, C))