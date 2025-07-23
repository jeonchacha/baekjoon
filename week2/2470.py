# 2470 두 용액
import sys
input = sys.stdin.readline
N = int(input().strip())
arr = list(map(int, input().split()))
arr.sort()
min_abs_sum = float('inf')
result = [None] * 2

left_pointer = 0
right_pointer = len(arr) - 1

while left_pointer != right_pointer:
    _sum = arr[left_pointer] + arr[right_pointer]
    if min_abs_sum > abs(_sum):
        min_abs_sum = abs(_sum)
        result[0], result[1] = arr[left_pointer], arr[right_pointer]

    if _sum == 0:
        break
    elif _sum < 0:
        left_pointer += 1
    else:
        right_pointer -= 1

print(result[0], result[1])