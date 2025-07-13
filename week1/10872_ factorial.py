# import sys

# N = int(sys.stdin.readline().strip())

# ans = 1
# if N == 0:
#     print(ans)
# else:
#     for i in range(1,N+1):
#         ans *= i
#     print(ans)

def factorial(n):
    # base case
    if n == 1:
        return 1
    # recursive case
    return n * factorial(n - 1)