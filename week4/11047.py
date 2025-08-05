# 11047 동전
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coins = [int(input().strip()) for _ in range(N)]

def min_coin_count(coins, n, amount):
    count = 0
    for i in range(n-1, -1, -1):
        count += amount // coins[i]
        amount %= coins[i]
    return count

print(min_coin_count(coins, N, K))