# SWEA 1463. 1로 만들기

N = int(input())

dp = [0] * 1000001  # dp 테이블

dp[1] = 0

for i in range(2, N + 1):
    # 3번 연산
    dp[i] = dp[i - 1] + 1

    # 1번 연산 수행 가능할 경우, 3번 연산 수행과 비교해 더 작은 값
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

    # 2번 연산 수행 가능할 경우, 3번 연산 수행과 비교해 더 작은 값
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[N])

