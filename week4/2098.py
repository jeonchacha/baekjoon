# 2098 외판원 순회
import sys
input = sys.stdin.readline

# 상태정의
# dp[current][visited]
# current: 현재 위치한 도시 (0 ~ N-1)
# visited: 비트마스크로 방문한 도시 집합 표현 (0 ~ 2^N - 1)
# 현재 current 도시에 있고, 
# 지금까지 방문한 도시의 집합이 visited일 때,
# 남은 도시를 방문하고 시작점으로 돌아가는 최소 비용

# 점화식
# dp[current][visited] = min(
#     dp[current][visited],
#     tsp[next][visited | (1 << next)] + w[current][next]
# )
# 단, 다음 조건을 만족해야 함:
# w[current][next] > 0 → 길이 존재해야 하고
# next 도시를 아직 방문하지 않았어야 함: (visited & (1 << next)) == 0

# 초기조건
# dp[0][1 << 0] = 0
# 0번 도시에서 시작했고, 방문한 도시는 0번 하나일 때, 비용은 0

# 종료조건
# 모든 도시를 다 방문한 상태 (visited == (1 << N) - 1) 에서
# 시작점으로 돌아가는 길이 있으면
# W[current][0]를 더해서 반환해야 함.
# (즉, 이 상태에서 dp[current][visited] + W[current][0])

N = int(input())  # 도시 수
W = [list(map(int, input().split())) for _ in range(N)]  # W[i][j] = i번 도시에서 j번 도시로 가는 비용

INF = float('inf')  # 길 없을 때 쓰기 위함

dp = [[INF] * (1 << N) for _ in range(N)]

def tsp(current, visited):
    # 종료 조건: 모든 도시를 방문했을 경우
    if visited == (1 << N) - 1:  # visited가 111...1이면 (모든 도시 방문)
        return W[current][0] if W[current][0] > 0 else INF  # 시작점(0)으로 돌아갈 수 있으면 비용, 없으면 INF

    # 이미 계산된 상태면 그 값을 그대로 리턴
    if dp[current][visited] != INF:
        return dp[current][visited]

    # 다음 도시 탐색
    for next in range(N):
        # 이미 방문한 도시면 건너뜀
        if visited & (1 << next):
            continue
        # 현재 도시에서 다음 도시로 가는 길이 없으면 건너뜀
        if W[current][next] == 0:
            continue

        cost = tsp(next, visited | (1 << next)) + W[current][next]
        dp[current][visited] = min(dp[current][visited], cost)

    return dp[current][visited]

# 시작점은 0번 도시, 0번 도시만 방문한 상태
print(tsp(0, 1 << 0))