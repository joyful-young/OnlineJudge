MAX = 40 * 3

def solution(info, n, m):
    N = len(info)
    # dp[i][j]: 물건 i까지 봤을 때 B의 흔적 개수가 j일 때의 A의 누적 흔적 개수
    dp = [[MAX for _ in range(m)] for _ in range(N + 1)]
    dp[0][0] = 0
    
    for i in range(1, N + 1):
        a, b = info[i - 1]
        for j in range(m):
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + a)
            
            if j + b < m:
                dp[i][j + b] = min(dp[i][j + b], dp[i - 1][j])
    
    answer = min(dp[N][i] for i in range(m))
    return answer if answer < n else -1