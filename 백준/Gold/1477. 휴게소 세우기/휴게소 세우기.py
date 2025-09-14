import sys
input = sys.stdin.readline


N, M, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr = [0] + arr + [L]

# 구간 간격
delta = [arr[i + 1] - arr[i] for i in range(N + 1)]


def needed_stops(d):
    # 각 구간을 길이 d 이하로 쪼개기 위해 필요한 휴개소 수
    cnt = 0
    for l in delta:
        cnt += (l - 1) // d
    return cnt


left = 1
right = max(delta)    # 현재 휴게소 없는 구간의 최대 길이
answer = right
while left <= right:
    mid = (left + right) // 2
    if needed_stops(mid) <= M:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)