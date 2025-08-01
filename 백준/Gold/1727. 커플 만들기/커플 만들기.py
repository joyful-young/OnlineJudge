import sys
input = sys.stdin.readline


MAX_DIFF = 1000000 * 1000


def min_total_diff(smaller, larger):
    s_len = len(smaller)
    l_len = len(larger)

    # dp[i][j]: i번, j번까지 고려했을 때 성격차 최소합
    dp = [[MAX_DIFF] * (l_len + 1) for _ in range(s_len + 1)]
    dp[0][0] = 0

    for i in range(s_len + 1):
        for j in range(l_len + 1):
            if i < s_len and j < l_len:
                diff = abs(smaller[i] - larger[j])
                # i와 j를 커플로 만들 경우 고려
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + diff)

            if j < l_len:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j])
    return dp[s_len][l_len]


M, F = map(int, input().split())
m_personality = list(map(int, input().split()))
f_personality = list(map(int, input().split()))

# 오름차순 정렬
m_personality.sort()
f_personality.sort()

if M <= F:
    print(min_total_diff(m_personality, f_personality))
else:
    print(min_total_diff(f_personality, m_personality))