# 11279 최대 힙
import sys
input = sys.stdin.readline
N = int(input().strip())
operate = [int(input().strip()) for _ in range(N)]

# 배열에 자연수 x를 넣는다. 삽입 shift up
# 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거한다. 삭제 shift down
heap = []

def insert(x):
    heap.append(x)
    # 부모 노드를 구해야하기에 추가한 마지막 인덱스, 즉 총길이 -1을 인자로
    shift_up(len(heap) - 1)

def shift_up(idx):
    parent = (idx - 1) // 2
    while idx > 0 and heap[parent] < heap[idx]:
        heap[parent], heap[idx] = heap[idx], heap[parent]
        idx = parent
        parent = (idx - 1) // 2

def pop():
    # 배열이 비어 있는 경우 출력하라고 하면 0 출력
    if not heap:
        print(0)
        return
    root = heap[0]
    last = heap.pop()
    if heap:
        heap[0] = last
        shift_down(0)
    print(root)

def shift_down(idx):
    n = len(heap)
    while True:
        left = idx * 2 + 1
        right = left + 1
        largest = idx

        # 두 자식 모두 검사해야 더 큰 값을 정확히 찾음
        if left < n and heap[left] > heap[largest]:
            largest = left
        if right < n and heap[right] > heap[largest]:
            largest = right
        
        if largest == idx:
            break
        
        heap[idx], heap[largest] = heap[largest], heap[idx]
        idx = largest

for i in operate:
    if i == 0:
        pop()
    else:
        insert(i)