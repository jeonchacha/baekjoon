# 백준 18258 큐2
import sys
input = sys.stdin.readline

def push(x):
    q.append(x)

def pop():
    if empty() == 1:
        print(-1)
        return
    
    global front_index
    val = q[front_index]
    front_index += 1
    print(val)
 
def size():
    print(len(q) - front_index)

def empty():
    return 1 if front_index >= len(q) else 0

def front():
    if empty() == 1:
        print(-1)
        return
    print(q[front_index])

def back():
    if empty() == 1:
        print(-1)
        return
    print(q[len(q) - 1])

front_index = 0
q = []

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
        print(empty())
    elif cmd == "front":
        front()
    elif cmd == "back":
        back()