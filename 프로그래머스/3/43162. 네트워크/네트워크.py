def solution(n, computers):
    visited = [False] * n
    answer = 0
    for s in range(n):
        if not visited[s]:
            stk = [s]
            visited[s] = True
            while stk:
                v = stk.pop()
                
                for w in range(n):
                    if not visited[w] and computers[v][w] == 1:
                        stk.append(w)
                        visited[w] = True
            answer += 1
    return answer

            