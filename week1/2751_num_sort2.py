import sys

n = int(sys.stdin.readline())
# 리스트 컴프리헨션
num_list = [int(sys.stdin.readline()) for _ in range(n)]

for i in sorted(num_list):
    print(i)

# 2750번 수 정렬하기
# 입력 크기 N이 최대 1,000까지
# 따라서 O(N^2) 의 단순 정렬 알고리즘(버블, 삽입, 선택)도 통과 가능

# 2751번 수 정렬하기2
# 입력 크기 N이 최대 1,000,000까지
# O(N^2) 알고리즘은 10^12번 연산이 돼 시간 초과, 반드시 O(nlogn) 이하의 알고리즘(병합, 힙, 퀵, Timsort) 을 사용해야 함
# O(nlogn) 은 N = 10^6 일때 약 20*10^6회 연산

# 파이썬의 sorted() .sort() 의 시간복잡도는 O(nlogn)