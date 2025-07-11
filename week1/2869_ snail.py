# N-1 * (A - B) + A >= V
import math

A, B, V = map(int,input().split())
if A >= V:
    print(1)
else:
    N = math.ceil((V - A) / ( A - B ) + 1)
    print(N)