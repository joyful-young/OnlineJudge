import sys
input = sys.stdin.readline


N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]

# A전봇대 위치 번호 오름차순
lines.sort()

b_lst = [lines[i][1] for i in range(N)]
# B전봇대 위치가 계속 증가하는 부분 수열
dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if b_lst[j] < b_lst[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))