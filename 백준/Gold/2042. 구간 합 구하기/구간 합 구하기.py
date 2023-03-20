# 백준 2042. 구간 합 구하기

import sys
input = sys.stdin.readline


def make_tree(node, start, end):
    if start == end:    # 리프 노드이면
        tree[node] = arr[start]     # 트리에 값을 적어주고
        return tree[node]   # 값 리턴

    mid = (start + end) // 2    # 중간 인덱스
    left_child = make_tree(2 * node, start, mid)     # 왼쪽 자식 노드 가서 재귀
    right_child = make_tree(2 * node + 1, mid + 1, end)   # 오른쪽 자식 노드 가서 재귀

    # 돌아오면 트리에 양쪽 자식 노드 합 더해서 값을 적어줌
    tree[node] = left_child + right_child
    return tree[node]


def get_sum(node, start, end):
    if c - 1 < start or b - 1 > end:    # 노드가 저장하고 있는 구간합 값의 구간이 범위를 벗어나는 경우
        return 0        # 더할 필요 없음
    if b - 1 <= start and end <= c - 1:     # 노드가 저장하고 있는 구간합 값의 구간이 범위 안에 있는 경우
        return tree[node]   # 그 구간합 값 리턴
    # 일부만 겹치는 경우
    mid = (start + end) // 2
    left_child = get_sum(2 * node, start, mid)  # 왼쪽으로
    right_child = get_sum(2 * node + 1, mid + 1, end)   # 오른쪽으로
    return left_child + right_child


def update(node, start, end):
    if b - 1 < start or b - 1 > end:        # 범위 밖이면
        return      # 중단

    if start == end:    # 리프 노드이면
        tree[node] = arr[start]     # 값 수정
        return

    mid = (start + end) // 2
    if start <= b - 1 <= mid:   # 왼쪽 구간에 포함되면
        update(2 * node, start, mid)
    else:       # 둘 중 한쪽에는 포함될 것. 왼쪽에 포함되지 않으면 오른쪽
        update(2 * node + 1, mid + 1, end)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]
    return


N, M, K = map(int, input().split())     # 수의 개수, 변경 횟수, 구간합을 구하는 횟수
arr = [0 for _ in range(N)]     # N개의 수 리스트

for i in range(N):
    arr[i] = int(input())

tree = [0 for _ in range(4 * N)]    # 세그먼트 트리 초기화
make_tree(1, 0, N - 1)
# print(tree)

for _ in range(M + K):
    a, b, c = map(int, input().split())

    # 숫자 수정
    if a == 1:
        arr[b - 1] = c
        update(1, 0, N - 1)
        # print(tree)

    # 구간합 구하기
    elif a == 2:
        print(get_sum(1, 0, N - 1))
        