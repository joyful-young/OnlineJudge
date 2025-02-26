def solution(info, n, m):
    """
    되도록 B가 훔쳐야
    B 흔적 허용치 넘으면 A도 훔쳐야
    A가 물건을 훔치면 B의 흔적이 줄어듦
    """
    N = len(info)
    all_b = sum([info[i][1] for i in range(N)])     # B가 다 훔칠 경우
    
    if all_b < m:
        return 0    # B가 모두 훔치는 게 가능할 때
    
    goal = all_b - m + 1    # 줄어들어야 하는 B의 흔적(goal 이상은 줄어들어야)
    
    # dp[x]: A 흔적이 x일 때 B 흔적이 줄어드는 양의 최댓값
    dp = [-1 for _ in range(n)]  # 인덱스: A의 흔적 0 ~ (n - 1)
    dp[0] = 0
    for a, b in info:
        for x in range(n - 1, a - 1, -1):
            if dp[x - a] != -1:
                dp[x] = max(dp[x], dp[x - a] + b)
    # print(dp)
    for idx, value in enumerate(dp):
        if value >= goal:
            return idx
    return -1