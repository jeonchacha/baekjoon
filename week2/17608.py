# 백준 17608번 막대기
import sys
input = sys.stdin.readline
N = int(input().strip())
heights = [int(input().strip()) for _ in range(N)]

ans = 0
max_h = 0
for i in range(N - 1, -1, -1):
    if heights[i] > max_h:
        ans += 1
        max_h = heights[i]
print(ans)