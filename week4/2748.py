# 2748 피보나치 수 2
import sys
input = sys.stdin.readline
N = int(input().strip())
dp = [0] * (N+1)
dp[1] = 1
def fibonacci(n):
    if n < 2:
        return n
    if dp[n] == 0:
        dp[n] = fibonacci(n-1) + fibonacci(n-2)
    return dp[n]

print(fibonacci(N))