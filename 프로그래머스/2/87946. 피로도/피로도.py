def solution(k, dungeons):
    N = len(dungeons)
    visited = [False for _ in range(N)]
    
    max_cnt = 0
    
    def perm(x, cur_k, cnt):
        nonlocal max_cnt
        if x == N:
            max_cnt = max(max_cnt, cnt)
            return
        
        for i in range(N):
            if not visited[i]:
                if dungeons[i][0] <= cur_k:
                    visited[i] = True
                    perm(x + 1, cur_k - dungeons[i][1], cnt + 1)
                    visited[i] = False
                else:
                    max_cnt = max(max_cnt, cnt)
                
    perm(0, k, 0)
    return max_cnt