import sys
sys.setrecursionlimit(10 ** 9)


def postorder(start, end):
    if start > end:
        return
    sub_root = end + 1      # 루트 노드보다 큰 값의 노드가 없었을 경우-> 오른쪽 트리 없음
    # postorder(sub_root, end)가 호출되었을 때 바로 리턴되도록 하기 위함.
    for i in range(start + 1, end + 1):     # 루트 노드를 제외한 노드
        if preorder[i] > preorder[start]:
            sub_root = i
            # print('sub_root', sub_root)
            break

    postorder(start + 1, sub_root - 1)      # 루트 노드 제외 왼쪽 트리에 있을 노드
    postorder(sub_root, end)                # 오른쪽 트리에 있을 노드
    print(preorder[start])          # 루트 노드


# 입력 받기. 입력 개수 주어지지 않음
preorder = []       # 전위순회결과

while True:
    try:
        preorder.append(int(sys.stdin.readline()))

    except:
        break


postorder(0, len(preorder) - 1)