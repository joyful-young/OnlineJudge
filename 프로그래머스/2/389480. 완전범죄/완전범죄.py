MAX = 120

def solution(info, n, m):
    N = len(info)   # 물건 개수
    # dp[i][j]: 물건 i까지 봤을 때 B 흔적이 j일 때의 A 흔적 최솟값
    dp = [[MAX] * m for _ in range(N + 1)]
    dp[0][0] = 0
    
    for i in range(1, N + 1):
        a, b = info[i - 1]
        
        for j in range(m):
            # A가 훔침
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + a)
            
            if j + b < m:
                # B가 훔침
                dp[i][j + b] = min(dp[i][j + b], dp[i - 1][j])
    
    answer = min(dp[N][i] for i in range(m))
    return answer if answer < n else -1