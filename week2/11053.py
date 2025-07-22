# 백준 11053번 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline
A = int(input().strip())
arr = list(map(int,input().split()))
lis = [arr[0]]

def binary_search(lis, start, end, x):
    if start > end:
        return start

    mid = (start + end) // 2
    if x == lis[mid]:
        return mid
    elif x > lis[mid]:
        return binary_search(lis, mid + 1, end, x)
    else:
        return binary_search(lis, start, mid - 1, x)

for x in arr[1:]:
    if x > lis[-1]:
        lis.append(x)
    else:
        idx = binary_search(lis, 0, len(lis) - 1, x)
        lis[idx] = x

print(len(lis))