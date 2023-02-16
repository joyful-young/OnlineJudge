# SWEA 1991. 트리 순회

import sys


def preorder(node):
    if node != '.':     # '.'가 아니면
        print(node, end='')     # 출력
        preorder(node_dict[node][0])    # 왼쪽 자식 노드로 이동해서 전위순회
        preorder(node_dict[node][1])    # 돌아와서 오른쪽 자식 노드로 이동해서 전위순회


def inorder(node):
    if node != '.':     # '.'가 아니면
        inorder(node_dict[node][0])     # 왼쪽 자식 노드로 가서 중위순회
        print(node, end='')             # 왼쪽 자식 다 돌고 루트노드 프린트
        inorder(node_dict[node][1])     # 오른쪽 자식 노드로 가서 중위순회


def postorder(node):
    if node != '.':
        postorder(node_dict[node][0])   # 왼쪽 자식 노드로 가서 후위순회
        postorder(node_dict[node][1])   # 오른쪽 자식 노드로 가서 후위순회
        print(node, end='')             # 루트노드 프린트


N = int(sys.stdin.readline())

node_dict = dict()

for _ in range(N):
    parent, left_child, right_child = sys.stdin.readline().rstrip().split()
    node_dict[parent] = left_child, right_child

# print(node_dict)

preorder('A')
print()
inorder('A')
print()
postorder('A')
