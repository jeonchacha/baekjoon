import sys
n = int(sys.stdin.readline())
num_list = []
while(n>0):
    num_list.append(int(sys.stdin.readline()))
    n -= 1

# 원본수정
num_list.sort()
# 내림차순
# num_list.sort(reverse=True)
# 원본수정 하지 않고 새 리스트 반환
# num_list_sorted = sorted(num_list)

for i in num_list:
    print(i)