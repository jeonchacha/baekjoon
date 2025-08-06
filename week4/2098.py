# 2098 외판원 순회

# 상태정의
# dp[current][visited]
# current: 현재 위치한 도시 (0 ~ N-1)
# visited: 비트마스크로 방문한 도시 집합 표현 (0 ~ 2^N - 1)
# 현재 current 도시에 있고, 
# 지금까지 방문한 도시의 집합이 visited일 때,
# 남은 도시를 방문하고 시작점으로 돌아가는 최소 비용

# 점화식
# dp[next][visited | (1 << next)] = min(
#     dp[next][visited | (1 << next)],
#     dp[current][visited] + W[current][next]
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

import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')
dp = [[INF] * (1 << N) for _ in range(N)]  # dp[current][visited]
dp[0][1 << 0] = 0  # 시작점은 0번 도시, 0번만 방문한 상태

for visited in range(1 << N):        # 방문한 도시 집합 순회
    for current in range(N):         # 현재 위치한 도시
        if dp[current][visited] == INF:
            continue  # 아직 도달하지 못한 상태라면 skip

        for next in range(N):        # 다음에 갈 도시
            if visited & (1 << next):    # 이미 방문한 도시면 skip
                continue
            if W[current][next] == 0:    # 길이 없으면 skip
                continue

            next_visited = visited | (1 << next)
            dp[next][next_visited] = min(
                dp[next][next_visited],
                dp[current][visited] + W[current][next]
            )

# 모든 도시를 방문한 상태에서 0번으로 돌아가는 최소 비용 계산
ans = INF
final_state = (1 << N) - 1  # visited == 111...1 → 모든 도시 방문한 상태

for last in range(N):
    if W[last][0] == 0:  # 마지막 도시에서 시작점으로 돌아갈 수 없으면 skip
        continue
    ans = min(ans, dp[last][final_state] + W[last][0])

print(ans)