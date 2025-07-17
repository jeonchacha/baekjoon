import sys
import itertools
n = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
# 브루트포스(순열)
n = len(num_list)
max_sum = 0
for i in itertools.permutations(num_list, n):
    temp_sum = 0
    print(i)
    for j in range(n-1):
        # abs(): 절대값
        temp_sum += abs(i[j] - i[j+1])
    if max_sum < temp_sum:
        max_sum = temp_sum
print(max_sum)