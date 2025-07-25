# 1991 트리 순회
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class Binary_tree:
    def __init__(self):
        self.root = None
    
    def preorder(self, node):
        if node == None:
            return []
        
        result = [node.item]
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        return result 
    
    def inorder(self, node):
        if node == None:
            return []
        
        result = []
        result += self.inorder(node.left)
        result.append(node.item)
        result += self.inorder(node.right)
        return result
    
    def postorder(self, node):
        if node == None:
            return []
        
        result = []
        result += self.postorder(node.left)
        result += self.postorder(node.right)
        result.append(node.item)
        return result

import sys
input = sys.stdin.readline
N = int(input().strip())
nodes = {}
for _ in range(N):
    parent, left, right = input().split()

    if parent not in nodes:
        nodes[parent] = Node(parent)
    
    if left != '.':
        if left not in nodes:
            nodes[left] = Node(left)
        nodes[parent].left = nodes[left]

    if right != '.':
        if right not in nodes:
            nodes[right] = Node(right)
        nodes[parent].right = nodes[right]

bt = Binary_tree()
root_label = list(nodes.keys())[0]
bt.root = nodes[root_label]
print(''.join(bt.preorder(bt.root)))
print(''.join(bt.inorder(bt.root)))
print(''.join(bt.postorder(bt.root)))