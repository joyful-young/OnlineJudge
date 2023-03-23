# 백준 1946. 신입 사원

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())    # 지원자 수

    arr = [tuple(map(int, input().split())) for _ in range(N)]

    arr.sort()      # 서류 순위 높은 지원자부터 정렬

    cnt = 1         # 첫번째 지원자는 선발 가능
    tmp = arr[0][1]     # 서류 1위의 면접 순위로 초기화
    for i in range(1, N):   # 두번째 지원자부터 확인
        if tmp > arr[i][1]:     # 이전 지원자 면접순위보다 높으면 선발 가능
            cnt += 1
            tmp = arr[i][1]

    print(cnt)