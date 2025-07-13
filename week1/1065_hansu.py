import sys

# 한수의 조건: 앞자리 - 중간자리 == 중간자리 - 끝자리
N = int(sys.stdin.readline().strip())

# 1~99까지는 다 한수
if N < 100:
    result = N
elif N >= 100:
    result = 99

for i in range(100, N+1):
    digits = list(map(int, str(i)))
    if len(digits) == 3:
        if digits[0] - digits[1] == digits[1] - digits[2]:
            result += 1

print(result)