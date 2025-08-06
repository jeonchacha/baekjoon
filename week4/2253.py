# 2253 점프
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split())
forbidden = [int(input().strip()) for _ in range(M)]

# 상태정의
# dp[i][k] = i번 돌에 "직전 점프 길이 k"로 도착하는 최소 점프 횟수

# 점화식
# i번 돌에 k로 도착했다면, 직전 상태는 다음 3가지 중 하나에서 올 수 있음:
# 1. i - k번 돌에서 k로 점프
# 2. i - (k - 1)번 돌에서 k - 1로 점프
# 3. i - (k + 1)번 돌에서 k + 1로 점프

# dp[i][k] = min(
#     dp[i - k][k],
#     dp[i - (k - 1)][k - 1],
#     dp[i - (k + 1)][k + 1]
# ) + 1
# 단, 각 상태가 유효한 돌일 경우에만 계산해야 함. 금지된 돌은 스킵

# 초기조건
# 1번 돌에서 출발, 처음 점프는 무조건 1칸으로 시작함 → dp[2][1] = 1
# 2번 돌이 금지된 돌이 아니어야만 이 초기 조건이 성립

dp = [[-1] * 251 for _ in range(N + 1)]
# why 251? k는 sqrt(2*N) 이하로 충분 (1+2+3+...+k >= N 이 되어야 하므로)

INF = float('inf')

def dfs(pos, k):
    # base case: 목적지 도달
    if pos == N:
        return 0
    
    # 범위 밖 or 금지된 돌이면 무효
    if pos > N or pos in forbidden:
        return INF
    
    # 이미 방문한 상태면 재사용
    if dp[pos][k] != -1:
        return dp[pos][k]
    
    min_jumps = INF

    # 다음 점프: k-1, k, k+1 (단, 1 이상일 때만)
    for next_k in [k - 1, k, k + 1]:
        if next_k >= 1:
            next_pos = pos + next_k
            cost = dfs(next_pos, next_k)
            if cost != INF:
                min_jumps = min(min_jumps, cost + 1)
    
    dp[pos][k] = min_jumps
    return dp[pos][k]

# 시작은 pos=1, k=0 (직전 점프 없음)
answer = dfs(1, 0)
print(answer if answer != INF else -1)
