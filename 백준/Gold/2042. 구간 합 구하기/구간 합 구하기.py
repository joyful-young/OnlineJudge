# 백준 2042. 구간 합 구하기 - 변수 수정

import sys
input = sys.stdin.readline


def make_tree(node, start, end):
    if start == end:    # 리프노드이면
        tree[node] = arr[start]     # 트리에 값을 적어주고
        return tree[node]   # 값 리턴

    mid = (start + end) // 2
    l_child = make_tree(2 * node, start, mid)   # 왼쪽 자식 노드 가서 재귀
    r_child = make_tree(2 * node + 1, mid + 1, end)     # 오른쪽 자식

    # 돌아오면 트리에 양쪽 자식 노드 합 더해서 값 적어줌
    tree[node] = l_child + r_child
    return tree[node]


def get_sum(node, start, end, l_idx, r_idx):
    if r_idx < start or l_idx > end:    # 노드가 저장하고 있는 구간합의 구간이 범위를 벗어나면
        return 0        # 더할 필요 없음
    if l_idx <= start and end <= r_idx:     # 노드가 저장하고 있는 구간합의 구간이 범위 내이면
        return tree[node]   # 그 구간합 리턴
    # 일부만 겹칠 경우
    mid = (start + end) // 2
    l_child = get_sum(2 * node, start, mid, l_idx, r_idx)     # 왼쪽으로
    r_child = get_sum(2 * node + 1, mid + 1, end, l_idx, r_idx)   # 오른쪽으로
    return l_child + r_child


def update(node, start, end, idx):
    if idx < start or idx > end:    # 범위 밖이면
        return      # 그쪽은 수정 안 함

    if start == end:    # 리프 노드이면
        tree[node] = arr[start]     # 값 수정
        return

    mid = (start + end) // 2
    if start <= idx <= mid:     # 왼쪽 구간에 포함되면
        update(2 * node, start, mid, idx)
    else:       # 둘 중 한쪽엔 포함됨. 오른쪽 구간에 포함되는 경우
        update(2 * node + 1, mid + 1, end, idx)

    tree[node] = tree[2 * node] + tree[2 * node + 1]
    return


N, M, K = map(int, input().split())     # 수의 개수, 변경 횟수, 구간합 구하는 횟수
arr = [int(input()) for _ in range(N)]

tree = [0 for _ in range(4 * N)]    # 세그먼트 트리
make_tree(1, 0, N - 1)      # 루트노드부터. 수열의 0 ~ (N - 1) 인덱스.

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:      # 숫자 수정
        idx = b - 1     # 수정할 숫자 인덱스
        arr[idx] = c
        update(1, 0, N - 1, idx)
    else:           # a가 2인 경우. 구간합 구하기
        l_idx = b - 1      # 인덱스로 바꿈
        r_idx = c - 1
        print(get_sum(1, 0, N - 1, l_idx, r_idx))
