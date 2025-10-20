import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, x, num):
        self.x = x
        self.num = num
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root
        
    def insert(self, x, num):
        node = self.root
        while True:
            if node.x > x:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(x, num)
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(x, num)
                    break
            
    def preorder(self, node, result):
        result.append(node.num)
        if node.left:
            self.preorder(node.left, result)
        if node.right:
            self.preorder(node.right, result)
        return result
    
    def postorder(self, node, result):
        if node.left:
            self.postorder(node.left, result)
        if node.right:
            self.postorder(node.right, result)
        result.append(node.num)
        return result
    
def solution(nodeinfo):
    answer = [[]]
    sorted_node = sorted([(node[0], node[1], i+1) for i, node in enumerate(nodeinfo)], key=lambda x: (-x[1], x[0]))
    # 1. 이진트리
    root = Node(sorted_node[0][0], sorted_node[0][2])
    tree = Tree(root)
    for i, (x, _, num) in enumerate(sorted_node):
        if i == 0:
            continue
        tree.insert(x, num)
    
    # 2. 전위/후위 순회
    answer = [tree.preorder(root, []), tree.postorder(root, [])]
    
    return answer

# [1,2,4,8,16,9,17,5,10,11,18,19,3,21,7,14,15]
# [1,2,4,8,16,9,17,5,10,11,18,19,3,6,12,13,20,21,7,14,15]