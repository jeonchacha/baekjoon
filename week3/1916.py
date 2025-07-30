# 1916 최소비용 구하기
import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))
start, end = map(int, input().split())

def dijkstra(adj_list, start, end):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (dist[start], start))  # (거리, 노드)

    while heap:
        cost, u = heapq.heappop(heap)
        
        if u == end:
            return cost
        
        if cost > dist[u]:
            continue
    
        for v, weigh in adj_list[u]:
            if dist[v] > dist[u] + weigh:
                dist[v] = dist[u] + weigh
                heapq.heappush(heap, (dist[v], v))
    return -1

print(dijkstra(adj_list, start, end))