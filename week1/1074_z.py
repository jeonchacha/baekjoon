import sys

N, r, c = map(int,sys.stdin.readline().split())

result = 0
def z(N, r, c):
    global result
    if N == 0:
        print(result)
        return
    
    half = 2**(N-1)
    area = half * half

    # 1사분면 
    if r < half and c < half:
        z(N-1, r, c)
    # 2사분면 area * 1
    elif r < half and c >= half:
        result += area
        z(N-1, r, c - half)
    # 3사분면 area * 2
    elif r >= half and c < half:
        result += area * 2
        z(N-1, r - half, c)
    # 4사분면 area * 3
    else:
        result += area * 3
        z(N-1, r - half, c - half)

z(N, r, c)