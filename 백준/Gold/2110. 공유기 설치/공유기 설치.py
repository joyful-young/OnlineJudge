# 백준 2110. 공유기 설치

import sys
input = sys.stdin.readline

N, C = map(int, input().split())    # 집의 개수, 공유기의 개수
home = [0 for _ in range(N)]
for i in range(N):
    home[i] = int(input())

home.sort()     # 집의 좌표 오름차순 정렬

left = 1    # 집 사이 최소 거리
right = home[-1] - home[0]  # 집 사이 최대 거리

while left <= right:
    mid = (left + right) // 2

    cnt = 1     # 공유기 설치된 집 수
    last = home[0]  # 마지막으로 설치된 공유기 위치
    # print('첫번째', mid, last)
    for i in range(1, N):       # 일단 mid 간격 이상으로 설치해 봄
        if home[i] - last >= mid:
            cnt += 1    # 공유기 설치
            last = home[i]      # 마지막 설치 위치 갱신
            # print('다음', mid, last)
    if cnt >= C:    # 끝까지 봤을 때 C개 이상이 설치되었으면
        ans = mid   # 답에 간격 mid를 저장하고 - 결국 탐색할 곳 더 없을 때까지 탐색하므로 최대 거리 나오게 됨
        left = mid + 1      # 더 큰 범위로 탐색해봄
    else:           # C개가 설치되지 못했으면
        right = mid - 1     # 더 작은 범위로 탐색해봄

print(ans)
