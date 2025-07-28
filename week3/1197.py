# 1197 최소 스패닝 트리
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) ## 안하면 런타임 에러

V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for i in range(E)]

def find(parent, x):
    if parent[x] != x:
         parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a != b:
        parent[b] = a

def kruscal(V, edges):
    parent = [i for i in range(V + 1)]
    edges.sort(key=lambda x:x[2])
    mst_weight = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_weight += w

    return mst_weight

mst_weight = kruscal(V, edges)
print(mst_weight)