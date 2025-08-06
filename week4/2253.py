# # 2253 점프

# # 상태정의
# # dp[i][k] = i번 돌에 "직전 점프 길이 k"로 도착하는 최소 점프 횟수

# # 점화식
# # i번 돌에 k로 도착했다면, 직전 상태는 다음 3가지 중 하나에서 올 수 있음:
# # 1. i - k번 돌에서 k로 점프
# # 2. i - (k - 1)번 돌에서 k - 1로 점프
# # 3. i - (k + 1)번 돌에서 k + 1로 점프

# # dp[i][k] = min(
# #     dp[i - k][k],
# #     dp[i - (k - 1)][k - 1],
# #     dp[i - (k + 1)][k + 1]
# # ) + 1
# # 단, 각 상태가 유효한 돌일 경우에만 계산해야 함. 금지된 돌은 스킵

# # 초기조건
# # 1번 돌에서 출발, 처음 점프는 무조건 1칸으로 시작함 → dp[2][1] = 1
# # 2번 돌이 금지된 돌이 아니어야만 이 초기 조건이 성립

import sys
input = sys.stdin.readline

# N: 마지막 돌 번호, M: 금지된 돌 개수
N, M = map(int, input().split())

# 금지된 돌들을 집합으로 저장 (O(1) 탐색용)
forbidden = set(int(input()) for _ in range(M))

# 점프 최대 길이의 실험적 상한선
# √(2 * 10^4) ≈ 141 → 여유 있게 250으로 설정
MAX_K = 250

# INF: 도달 불가능을 의미하는 초기값
INF = float('inf')

# dp[pos][k]: pos 위치에 점프 길이 k로 도착한 최소 점프 횟수
dp = [[INF] * (MAX_K + 1) for _ in range(N + 1)]

# 초기 조건 설정
# 1번 돌에서 2번 돌로 jump=1로 이동한 경우만 가능
# 단, 2번 돌이 금지된 돌이면 도달 불가
if 2 not in forbidden:
    dp[2][1] = 1  # jump 1로 한 번 점프한 것이므로 1

# 점화식 기반 bottom-up dp
# 3번 돌부터 N번 돌까지 순차적으로 점검
for pos in range(3, N + 1):

    # 금지된 돌이면 무시하고 스킵
    if pos in forbidden:
        continue

    # 점프 길이 k = 현재 도착할 때 쓴 점프 길이
    for k in range(1, MAX_K + 1):

        # 이전 점프 길이로 가능한 후보들: (k-1, k, k+1)
        for prev_k in (k - 1, k, k + 1):
            prev_pos = pos - k  # 현재 위치로 점프하기 전의 위치

            # 유효한 점프 길이와 위치인지 확인 (경계 조건 체크)
            if 1 <= prev_k <= MAX_K and 1 <= prev_pos <= N:

                # 이전 위치에 prev_k로 도달 가능한 경우만 고려
                if dp[prev_pos][prev_k] != INF:

                    # 현재 pos에 k로 도달 가능한 최소 점프 횟수 갱신
                    dp[pos][k] = min(dp[pos][k], dp[prev_pos][prev_k] + 1)

# N번 돌에 도달 가능한 모든 점프 길이 중 최소값 탐색
answer = min(dp[N])

# 도달 가능하면 최소 점프 횟수 출력, 불가능하면 -1 출력
print(answer if answer != INF else -1)