# 5639 이진 검색 트리
# 트리 자체를 만들 필요 없이 전위 순회의 인덱스 구간만으로 후위 순회를 처리
import sys
input = sys.stdin.read  # read()는 EOF까지 한 번에 입력 받아줌
sys.setrecursionlimit(10**6)

preorder = list(map(int, input().split()))  # split()은 줄바꿈 포함 모든 공백 기준으로 나눔 (\n, 스페이스 등)

def postorder(start, end):
    if start > end: return

    root = preorder[start]  # 현재 부분트리의 루트는 전위 순회의 맨 앞
    idx = start + 1
    while idx <= end and preorder[idx] < root:
        idx += 1
    
    postorder(start + 1, idx - 1)
    postorder(idx, end)
    print(root)
    
postorder(0, len(preorder) - 1)