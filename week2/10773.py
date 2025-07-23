# 10773 제로
import sys
input = sys.stdin.readline
K = int(input().strip())
stack = [int(input().strip()) for _ in range(K)]
ans = []
for i in stack:
    if i == 0:
        ans.pop()
    else:
        ans.append(i)
print(sum(ans))