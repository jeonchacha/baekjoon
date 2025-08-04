# 9084 동전
import sys
input = sys.stdin.readline
T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    coins = list(map(int, input().split()))
    M = int(input().strip())

    def make_amount(n, coins, amount):
        # coins.insert(0,0) -> 원본의 내용을 바꾸기 때문에 side effect 발생 가능성 있음
        coins = [0] + coins     # 새로운 리스트 생성
        # 상태정의 : 
        #   dp[n][amount] = n번째까지의 동전을 사용해서 amount를 만드는 경우의 수 
        dp = [[0] * (amount+1) for _ in range(n+1)]
        # 초기조건 :
        #   dp[0][0] = 1        0원을 만드는 방법은 항상 1가지 (아무 동전도 안 씀)
        #   dp[0][amount] = 0   동전이 없으면 금액을 만들 수 없음
        #   dp[n][0] = 1        0원을 만드는 방법은 항상 1가지 (아무 동전도 안 씀)
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, amount+1):
                if j >= coins[i]:
                    dp[i][j] = dp[i - 1][j]     # i번째 동전을 안쓰고 j원
                    + dp[i][j - coins[i]]       # i번째 동전을 한번 쓰고 j원 -> 남은 금액을 DP로 또 해결
                else:
                    dp[i][j] = dp[i - 1][j]     # i번째 동전을 쓸 때 금액이 음수가 되면 못씀 
        return dp[n][amount]

    result = make_amount(N, coins, M)
    print(result)

