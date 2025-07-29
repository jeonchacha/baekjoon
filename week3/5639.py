# 5639 이진 검색 트리
import sys
input = sys.stdin.read  # read()는 EOF까지 한 번에 입력 받아줌
sys.setrecursionlimit(10**6)

preorder = list(map(int, input().split()))  # split()은 줄바꿈 포함 모든 공백 기준으로 나눔 (\n, 스페이스 등)

# 전위 순회 리스트로부터 루트/왼/오를 인덱스로 나눔
# 각 서브트리에 대해 재귀적으로 다시 후위 순회 방식(왼->오->루트) 적용
# 트리를 만들지 않고 인덱스로만 분할해서 해결
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