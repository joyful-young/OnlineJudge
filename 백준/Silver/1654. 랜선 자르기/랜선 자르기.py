# 백준 1654. 랜선 자르기

import sys
input = sys.stdin.readline

K, N = map(int, input().split())

arr = [0 for _ in range(K)]     # K개의 랜선
for i in range(K):
    arr[i] = int(input())

start = 1   # 만들 랜선 최소 길이
end = max(arr)      # 만들 수 있는 랜선 최대 길이

while start <= end:
    mid = (start + end) // 2    # 새롭게 만들 랜선의 길이

    tmp = 0     # 만들 수 있는 랜선 개수
    for i in range(K):
        tmp += arr[i] // mid

    if tmp >= N:        # N개 이상 만들 수 있으면 값 일단 답에 저장하고 길이 더 늘릴 수 있는지 확인
        ans = mid
        start = mid + 1
    else:               # N개를 만들 수 없으면 만들 랜선 길이 줄여서 다시 확인
        end = mid - 1

print(ans)