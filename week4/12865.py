# 12865 아주 평범한 배낭
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
weights = [0] * (N+1)
values = [0] * (N+1)
for i in range(1, N+1):
    w, v = map(int, input().split())
    weights[i] = w
    values[i] = v

def knapsack(N, K, weights, values):
    dp = [[0] * (K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, K+1):
            if j >= weights[i]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - weights[i]] + values[i])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][K]

result = knapsack(N, K, weights, values)
print(result)