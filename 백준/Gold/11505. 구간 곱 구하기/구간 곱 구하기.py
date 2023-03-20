# 백준 11505. 구간 곱 구하기

import sys
input = sys.stdin.readline
div = 1000000007


def make_tree(node, start, end):
    if start == end:    # 루트 노드
        tree[node] = arr[start]
        return tree[node] % div

    mid = (start + end) // 2
    l_child = make_tree(2 * node, start, mid)
    r_child = make_tree(2 * node + 1, mid + 1, end)
    tree[node] = l_child * r_child % div
    return tree[node]


def get_product(node, start, end, l_idx, r_idx):
    if r_idx < start or l_idx > end:    # 범위 벗어나면
        return 1
    if l_idx <= start and end <= r_idx:     # 범위 내이면
        return tree[node] % div

    # 일부만 겹칠 경우
    mid = (start + end) // 2
    l_child = get_product(2 * node, start, mid, l_idx, r_idx)
    r_child = get_product(2 * node + 1, mid + 1, end, l_idx, r_idx)
    return l_child * r_child % div


def update(node, start, end, idx):
    if idx < start or idx > end:    # 범위 밖이면
        return
    if start == end:        # 리프 노드이면
        tree[node] = c      # 값 수정
        return

    mid = (start + end) // 2
    if start <= idx <= mid:     # 왼쪽 구간에 포함
        update(2 * node, start, mid, idx)
    else:
        update(2 * node + 1, mid + 1, end, idx)

    tree[node] = tree[2 * node] * tree[2 * node + 1] % div
    return


N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

tree = [0 for _ in range(4 * N)]
make_tree(1, 0, N - 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:      # 값 수정
        idx = b - 1
        arr[idx] = c
        update(1, 0, N - 1, idx)

    else:           # 구간곱 출력
        l_idx = b - 1
        r_idx = c - 1
        print(get_product(1, 0, N - 1, l_idx, r_idx))