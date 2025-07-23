# 11866 요세푸스 문제 0
import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())

queue = deque(range(1, N + 1))
result = []
while queue:
    # for _ in range(K - 1):
    #     queue.append(queue.popleft())
    queue.rotate(-(K - 1))
    result.append(queue.popleft())

print("<" + ", ".join(map(str, result)) + ">")