# 2493 탑
import sys
input = sys.stdin.readline
N = int(input().strip())
H = list(map(int, input().split()))
stack = []
result = []

for idx, val in enumerate(H):

    while stack and stack[-1][1] < val:
        stack.pop()
    
    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][0])

    stack.append((idx + 1, val))

print(" ".join(map(str, result)))