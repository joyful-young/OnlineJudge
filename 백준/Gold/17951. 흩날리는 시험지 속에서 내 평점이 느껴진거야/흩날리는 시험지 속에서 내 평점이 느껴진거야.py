# 백준 17951. 흩날리는 시험지 속에서 내 평점이 느껴진거야
N, K = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = N * 20      # 맞은 문제 최대 개수

maxV = 0
while left <= right:
    mid = (left + right) // 2   # 이걸 최솟값으로 하는 K개 그룹을 만들 수 있는지

    tmp = 0         # 현재 만드는 중인 그룹의 맞은 문제 수
    group = 0       # 현재 만들어진 그룹 수
    for i in range(N):
        tmp += arr[i]

        if tmp >= mid:      # 최솟값 이상이면
            group += 1      # 그룹 하나 만들어짐
            tmp = 0         # 초기화

        if group >= K:      # 그룹의 수가 K를 넘으면 각 그룹 최솟값이 mid 이상인 경우가 나온다는 의미
            maxV = max(maxV, mid)
            left = mid + 1      # 가능한 더 큰 값이 있는지 확인하기 위해 left 옮김
            break               # for문 break. while문 새로 반복
    else:       # group의 수가 K를 넘지 못했으면 mid 줄여봐야
        right = mid - 1

print(maxV)