# 백준 12852. 1로 만들기 2

N = int(input())

dp = [[0 for _ in range(2)] for _ in range(max(4, N + 1))]      # 0에서 N까지

# dp[n][0]: n을 1로 만드는 연산 횟수 최솟값
# dp[n][1]: 최소값이 나올 수 있는 연산 결과

dp[1][0] = 0
dp[1][1] = 1
dp[2][0] = 1
dp[2][1] = 1
dp[3][0] = 1
dp[3][1] = 1

if N > 3:
    for i in range(4, N + 1):
        if i % 3 == 0 and i % 2 == 0:   # 2와 3의 공배수
            min_dp = min(dp[i // 3][0], dp[i // 2][0], dp[i - 1][0])
            dp[i][0] = min_dp + 1

            if min_dp == dp[i // 3][0]:
                dp[i][1] = i // 3
            elif min_dp == dp[i // 2][0]:
                dp[i][1] = i // 2
            else:
                dp[i][1] = i - 1

        elif i % 3 == 0:    # 3의 배수
            min_dp = min(dp[i // 3][0], dp[i - 1][0])
            dp[i][0] = min_dp + 1

            if min_dp == dp[i // 3][0]:
                dp[i][1] = i // 3
            else:
                dp[i][1] = i - 1

        elif i % 2 == 0:            # 2의 배수
            min_dp = min(dp[i // 2][0], dp[i - 1][0])
            dp[i][0] = min_dp + 1

            if min_dp == dp[i // 2][0]:
                dp[i][1] = i // 2
            else:
                dp[i][1] = i - 1

        else:
            dp[i][0] = dp[i - 1][0] + 1
            dp[i][1] = i - 1

    print(dp[N][0])
    print(N, end=' ')
    while N != 1:
        N = dp[N][1]
        print(N, end=' ')

else:
    print(dp[N][0])
    print(N, end=' ')
    while N != 1:
        N = dp[N][1]
        print(N, end=' ')

