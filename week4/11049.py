# 11049 행렬 곱셈 순서
import sys
input = sys.stdin.readline
n = int(input().strip())
p = []
for i in range(n):
    row, col = map(int, input().split())

    if i == 0:
        p.append(row)
    p.append(col)

# 상태정의
# dp[i][j] = 행렬 Ai ~ Aj 까지 곱할 때 최소 곱셈 연산 수
# 예: dp[1][3] → 행렬 A1 × A2 × A3의 곱셈 최소 연산 수

# 점화식
# dp[i][j] = min(dp[i][k] + dp[k+1][j] + p[i-1] × p[k] × p[j])
# 각 서브문제(왼쪽, 오른쪽 부분 행렬 곱) 비용 + 두 결과 행렬 곱 비용

# 초기조건
# dp[i][i] = 0 
# → Ai 하나만 있는 경우 곱셈 필요 없음

# 예제 입력: 행렬 3개 (A₁, A₂, A₃)
# 각 행렬 Ai의 크기는 p[i-1] × p[i]
# p = [5, 3, 2, 6]
# A₁: 5×3
# A₂: 3×2
# A₃: 2×6

def matrix_chain_order(p):
    n = len(p) - 1  # 행렬 개수
    dp = [[0] * (n + 1) for _ in range(n + 1)]  # dp[i][j] = Ai ~ Aj 최소 곱셈 수

    for length in range(2, n + 1):  # length = 부분행렬 개수, 2부터 시작
        for i in range(1, n - length + 2):  # 시작 인덱스
            j = i + length - 1  # 끝 인덱스
            dp[i][j] = float('inf')

            for k in range(i, j):  # 분할 위치
                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n]  # A1 ~ An까지 최소 곱셈 연산 수

min_cost = matrix_chain_order(p)
print(min_cost)