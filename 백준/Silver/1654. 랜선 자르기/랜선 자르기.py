# 백준 1654 랜선 자르기

# 갖고 있는 랜선 개수 K, 필요한 랜선 개수 N
# N개를 만들 수 있는 랜선의 최대 길이 출력

import sys

K, N = map(int, sys.stdin.readline().split())
lans = [0] * K

# 갖고 있는 랜선 길이 리스트 완성
for i in range(K):
    lans[i] = int(sys.stdin.readline())

# 랜선 길이 범위
start = 0
end = max(lans)

while start <= end:
    mid = (start + end) // 2

    # K = 1, N = 1, 1 -> ZeroDivisionError
    if mid == 0:
        print(end)
        break

    # 얻은 랜선 개수 초기화
    get_N = 0

    # 얻으려는 랜선 길이 mid일 때 얻을 수 있는 랜선 개수 계산
    for length in lans:
        get_N += length // mid

    # 원하는 개수보다 작으면 랜선 길이 줄임
    if get_N < N:
        end = mid - 1
    # elif get_N == N:
    #     print(mid)
    #     break
    else:
        start = mid + 1
# break 되지 않고 반복 종료했으면
else:
    print(end)

