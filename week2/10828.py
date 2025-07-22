# 백준 10828번 스택
import sys
input = sys.stdin.readline

def push(x):
    global _top
    if _top + 1 == len(stack):
        print("stack overflow")
        return
    _top += 1
    stack[_top] = x

def pop():
    global _top
    if _top == -1:
        print(-1)
        return
    val = stack[_top]
    _top -= 1
    print(val)

def size():
    print(_top + 1)

def empty():
    print(1 if _top == -1 else 0)

def top():
    if _top == -1:
        print(-1)
        return
    print(stack[_top])

stack = [None] * 10000
_top = -1

N = int(input().strip())
for _ in range(N):
    parts = input().split()
    cmd = parts[0]
    if cmd == "push":
        push(int(parts[1]))
    elif cmd == "pop":
        pop()
    elif cmd == "size":
        size()
    elif cmd == "empty":
        empty()
    elif cmd == "top":
        top()    