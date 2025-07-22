# 백준 2805번 나무 자르기

import sys
input = sys.stdin.readline
N, M = map(int,input().split())
tree = list(map(int,input().split()))

def bisect_right(tree, H):
    left = 0
    right = len(tree) - 1
    result = len(tree)      # 만약 모든 원소가 H보다 작으면 len(tree) 반환

    while left <= right:
        mid = (left + right) // 2
        if H <= tree[mid]:
            result = mid
            right = mid - 1     # 왼쪽 절반에 더 작은 인덱스가 없는지 탐색
        else:
            left = mid + 1
    return result

tree.sort()
left = 0
right = tree[len(tree) - 1]
answer = 0
while left <= right:
    H = (left + right) // 2     # 톱날 높이
    
    wood = 0
    idx = bisect_right(tree, H)
    for height in tree[idx:]:
        wood += (height - H)

    if wood >= M:
        answer = H
        left = H + 1
    else:
        right = H - 1
print(answer)