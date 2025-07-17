# 백준 1920번 수 찾기
import sys
input = sys.stdin.readline
N = int(input())
N_list = list(map(int,input().split()))
M = int(input())
M_list = list(map(int,input().split()))

def binary_search(n_list, start, end, target):
    if start > end:
        print(0)
        return
    
    mid = (start + end) // 2

    if n_list[mid] == target:
        print(1)
        return
    elif n_list[mid] > target:
        binary_search(n_list, start, mid - 1, target)
    else:
        binary_search(n_list, mid + 1, end, target)

sorted_N_list = sorted(N_list)
for i in M_list:
    binary_search(sorted_N_list, 0, len(sorted_N_list) - 1, i)