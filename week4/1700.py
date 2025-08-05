# 1700 멀티탭 스케줄링
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
item = list(input().split())

def schedule(n, item):
    a = []
    for i in range(n):
        a.append(item[i])
    count = 0
    for i in item[n+1:]:
        for j in a:
            if i == j:
                break
        else:
            a[-1] = i
            count += 1

    return count

print(schedule(N, item))