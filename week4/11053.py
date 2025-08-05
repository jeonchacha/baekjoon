# 11053 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline
N = int(input().strip())
sequence = list(map(int, input().split()))

def lis(n, sequence):
    # 초기조건: dp[i] = 1 -> 자기 자신만 포함하는 LIS
    # 상태정의: dp[i] = i 번째 수를 마지막 원소로 갖는 LIS 
    dp = [1] * n  
    for i in range(n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    # [0, 10, 20, 30] 일때 dp[3] 이면 3 이지만 [0, 10, 20, 30, 15] 일때 dp[4] = 2
    # 그래서 max 값을 리턴
    return max(dp)

print(lis(N, sequence))