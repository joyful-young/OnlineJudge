# 백준 2805. 나무 자르기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

start = 0   # 절단기 높이 최솟값
end = max(arr)  # 절단기 높이 최댓값(가장 큰 나무 높이)

while start <= end:
    mid = (start + end) // 2

    tree = 0    # 집에 가져갈 나무 길이
    for height in arr:
        if height > mid:    # 절단기 높이보다 나무가 높으면
            tree += height - mid    # 높은 만큼 집에 가져갈 나무에 추가

    if tree > M:   # M미터 이상의 길이가 나오면 일단 값 저장하고 높이를 높여서 다시 확인
        ans = mid
        start = mid + 1
    elif tree == M:
        ans = mid
        break
    else:           # M미터가 안 되면 높이 낮춰서 다시 확인
        end = mid - 1
print(ans)