# 9012 괄호
import sys
input = sys.stdin.readline
T = int(input().strip())
PS = [list(input().strip()) for _ in range(T)]

for ps in PS:
    def is_VPS(ps):
        stack = []
        for i in ps:
            if i == '(':
                stack.append('(')
            else:
                if stack:
                    stack.pop()
                else:
                    print('NO')
                    return
        if stack:
            print('NO')
        else:
            print('YES')

    is_VPS(ps)