import sys
input = sys.stdin.readline

N = int(input())
arr = [0 for _ in range(N)]
for i in range(1, N + 1):
    t, p = map(int, input().split())
    # [상담 시작 날짜, 상담이 끝나서 이익이 들어오는 날짜, 이익]
    arr[i - 1] = [i, i + t, p]

dp = [0 for _ in range(N + 2)]

for i in range(1, N + 2):
    dp[i] = dp[i - 1]
    # i일까지 나온 상담 일정
    for s, e, p in arr[:i]:
        if i == e:
            dp[i] = max(dp[i], dp[s] + p)

print(dp[N + 1])