# 백준 11066. 파일 합치기
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    K = int(input())
    arr = list(map(int, input().split()))

    dp = [[0 for _ in range(K)] for _ in range(K)]

    prefix_sum = {-1: 0}
    for i in range(K):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i]

    # 파일을 두 구간으로 나눠서 각 구간을 하나의 파일로 합치는 최소 비용을 구한다
    # dp[i][j]: i ~ j 구간 합치는 최소비용
    # 구간 길이 1인 것부터 구하기
    for l in range(1, K):
        for i in range(K - l):      # 구간 시작 0 ~ (K - l)
            tmp = float('inf')
            s = i
            e = i + l
            for d in range(s, e):   # 구간을 (i ~ d), (d + 1 ~ i + l)로 자름
                # 원래 값과 비교해서 더 작은 값
                # 앞구간 최소비용 + 뒷구간 최소비용 + 전체 구간합
                tmp = min(tmp, dp[s][d] + dp[d + 1][e])

            dp[s][e] = tmp + prefix_sum[e] - prefix_sum[s - 1]

    print(dp[0][K - 1])
