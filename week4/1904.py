# 1904 01타일
import sys
input = sys.stdin.readline
N = int(input().strip())

def get_tile(n):
    if n < 2:
        return n
    dp = [0] * (N+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N+1):
        # 1로 끝나는 경우 + 00으로 끝나는 경우
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    return dp[n]

print(get_tile(N))