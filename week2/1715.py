# 1715 카드 정렬하기
import sys
import heapq
input = sys.stdin.readline
N = int(input().strip())
cards = [int(input().strip()) for _ in range(N)]

heapq.heapify(cards)
total_cost = 0

while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    cost = a + b
    total_cost += cost
    heapq.heappush(cards, cost)

print(total_cost)

# MaxHeap으로 쓰는 핵심 아이디어
# 값을 음수로 바꿔서 넣고 꺼낼 때 다시 양수로 돌리면 됨 
# 삽입 : heapq.heappush(heap, -x)
# 꺼내기 : -heapq.heappop(heap)
# 가장 큰 값 확인 : -head[0]