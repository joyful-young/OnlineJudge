from collections import deque

def solution(n, edge):
    def count_farthest_nodes(start):
        visited = [-1 for _ in range(n + 1)]
        visited[start] = 0
        
        q = deque([start])
        while q:
            v = q.popleft()
            
            for w in adjL[v]:
                if visited[w] == -1:
                    visited[w] = visited[v] + 1
                    q.append(w)
                    
        cnt = 0
        max_v = 0
        for i in range(1, n + 1):
            if visited[i] > max_v:
                cnt = 1
                max_v = visited[i]
            elif visited[i] == max_v:
                cnt += 1
        print(visited)
        return cnt
    
    
    adjL = [[] for _ in range(n + 1)]
    for a, b in edge:
        adjL[a].append(b)
        adjL[b].append(a)
    
    return count_farthest_nodes(1)