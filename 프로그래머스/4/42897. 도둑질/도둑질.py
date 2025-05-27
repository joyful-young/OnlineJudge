def solution(money):
    N = len(money)
    # steal[0][i]: 0번 집을 털었을 경우, i번 집까지 확인해서 i번 집은 안 털었을 경우 돈 최댓값
    # steal[1][i]: 0번 집을 털었을 경우, i번 집까지 확인해서 i번 집을 털었을 경우 돈 최댓값
    steal = [[0] * N for _ in range(2)]
    not_steal = [[0] * N for _ in range(2)]
     
    steal[1][0] = money[0]
    for i in range(1, N):
        steal[0][i] = max(steal[0][i - 1], steal[1][i - 1])
        steal[1][i] = steal[0][i - 1] + money[i]
        
        not_steal[0][i] = max(not_steal[0][i - 1], not_steal[1][i - 1])
        not_steal[1][i] = not_steal[0][i - 1] + money[i]
    
    return max(steal[0][N - 1], not_steal[0][N - 1], not_steal[1][N - 1])