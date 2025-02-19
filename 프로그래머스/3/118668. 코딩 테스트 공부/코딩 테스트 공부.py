from heapq import heappush, heappop

def solution(alp, cop, problems):
    N = len(problems)
    # 모든 문제를 푸는 데 추가적으로 필요한 알고력 & 코딩력
    required_alp = max(max([problems[i][0] for i in range(N)]) - alp, 0)
    required_cop = max(max([problems[i][1] for i in range(N)]) - cop, 0)
    
    # dp[a][c]: a 알고력, c 코딩력을 추가로 높이기 위한 최소 비용
    dp = [[300 for _ in range(required_cop + 1)] for _ in range(required_alp + 1)]
    dp[0][0] = 0
    
    problems = problems + [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
    q = [[0, [0, 0]]]   # [비용, [추가 알고력, 추가 코딩력]]
    while q:
        cost, power = heappop(q)
        
        if power[0] >= required_alp and power[1] >= required_cop:
            break
        
        for alp_req, cop_req, alp_rwd, cop_rwd, time in problems:
            if can_solve(alp + power[0], cop + power[1], alp_req, cop_req):
                # 문제를 푼 후의 값
                a, c = min(power[0] + alp_rwd, required_alp), min(power[1] + cop_rwd, required_cop)
                new_cost = cost + time
                if dp[a][c] > new_cost:
                    dp[a][c] = new_cost
                    heappush(q, [new_cost, [a, c]])
        
    return dp[required_alp][required_cop]


def can_solve(alp, cop, alp_req, cop_req):
    return alp_req <= alp and cop_req <= cop