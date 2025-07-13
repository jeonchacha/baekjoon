import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(n)]

# 정렬 후 set 으로 변환하면 순서가 사라짐
words = list(set(words))
words.sort()
words.sort(key=len)

for i in words:
    print(i)