# 백준 19637. if문 좀 대신 써줘

import sys

N, M = map(int, sys.stdin.readline().split())

name_score_lst = list()
for _ in range(N):
    a, b = sys.stdin.readline().split()
    name_score_lst.append([a, int(b)])

for _ in range(M):
    input_score = int(sys.stdin.readline())
    start_idx = 0
    end_idx = N - 1
    while start_idx <= end_idx:
        mid_idx = (start_idx + end_idx) // 2
        if input_score <= name_score_lst[mid_idx][1]:    # 구간 중간 점수 이하이면
            # 인덱스가 0이거나 전 단계 칭호 상한보다 크면 칭호 결정
            if mid_idx == 0 or (mid_idx != 0 and input_score > name_score_lst[mid_idx - 1][1]):
                print(name_score_lst[mid_idx][0])
                break
            else:
                end_idx = mid_idx - 1

        else:       # 구간 중간 점수 초과
            start_idx = mid_idx + 1


