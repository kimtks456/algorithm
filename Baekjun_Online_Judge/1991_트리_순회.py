import sys


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.child = []

n = int(input())
tree = [[] for _ in range(26)]

# Tree Build
for i in range(n):
    p, c1, c2 = sys.stdin.readline().split()
    child = tree[ord(p) - ord('A')]
    child.append(c1)
    child.append(c2)


def preorder(pre, target):
    pre.append(target)
    for c in tree[ord(target) - ord('A')]:
        if c != '.':
            preorder(pre, c)


def inorder(ind, target):
    child = tree[ord(target) - ord('A')]
    if child[0] != '.':
        inorder(ind, child[0])
    ind.append(target)
    if child[1] != '.':
        inorder(ind, child[1])


def postorder(post, target):
    for c in tree[ord(target) - ord('A')]:
        if c != '.':
            postorder(post, c)
    post.append(target)


pre, ind, post = [], [], []

preorder(pre, 'A')
inorder(ind, 'A')
postorder(post, 'A')

print(''.join(pre))
print(''.join(ind))
print(''.join(post))
