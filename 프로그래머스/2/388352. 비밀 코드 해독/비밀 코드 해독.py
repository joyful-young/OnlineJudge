N = 5

def solution(n, q, ans):
    m = len(q)
    answer = 0
    
    c = [0 for _ in range(N)]
    numbers = [i for i in range(1, n + 1)]
    
    
    def comb(r, s):
        nonlocal answer
        if r == 0:
            code_num_set = set(c)
            for i in range(m):
                cnt = 0
                for j in range(N):
                    if q[i][j] in code_num_set:
                        cnt += 1
                if cnt != ans[i]:
                    break
            else:
                 answer += 1   
            return
        
        for i in range(s, n - r + 1):
            c[r - 1] = numbers[i]
            comb(r - 1, i + 1)
    
    
    
    comb(N, 0)
    return answer

