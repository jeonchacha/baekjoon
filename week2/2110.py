# 2110 공유기 설치
import sys
input = sys.stdin.readline
N, C = map(int, input().split())

houses = [int(input().strip()) for _ in range(N)]
answer = 0

# 최소 거리 D를 유지하면서 공유기를 C개 이상 설치할 수 있는지?
# D: 이번에 판단하고 있는 거리
def can_install(houses, D, C):
    count = 1
    prev = houses[0]
    for i in houses[1:]:
        if i - prev >= D:
            count += 1
            prev = i # 설치한 경우에만 갱신 해야함
    return count >= C

def binary_search(houses, lo, hi, C):
    global answer

    if lo > hi:
        return 0 # 탐색 실패 시 반환값 없음
    
    mid = (lo + hi) // 2
    is_installed = can_install(houses, mid, C)
    
    if is_installed:
        answer = mid
        return binary_search(houses, mid + 1, hi, C)
    else:
        return binary_search(houses, lo, mid - 1, C)

houses.sort()
binary_search(houses, 1, houses[-1] - houses[0], C)
print(answer)