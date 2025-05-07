dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solution(storage, requests):
    storage = list(map(list, storage))
    n, m = len(storage), len(storage[0])
    
    containers = {}
    for i in range(n):
        for j in range(m):
            if storage[i][j] in containers:
                containers[storage[i][j]].add((i, j))
            else:
                containers[storage[i][j]] = {(i, j)}
    
    for request in requests:
        if request[0] not in containers:
            continue
        
        if len(request) == 2:
            for r, c in containers[request[0]]:
                storage[r][c] = ""
            del containers[request[0]]
        else:
            taken = set()
            for r, c in containers[request[0]]:
                if can_take_out(r, c, storage):
                    taken.add((r, c))
            
            for r, c in taken:
                storage[r][c] = ""
            
            containers[request[0]] -= taken
            if not containers[request[0]]:
                del containers[request[0]]

    return sum(len(v) for v in containers.values())


def can_take_out(sr, sc, storage):
    stack = [(sr, sc)]
    
    n, m = len(storage), len(storage[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[sr][sc] = True
    
    while stack:
        r, c = stack.pop()
        
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            
            if not (0 <= nr < n and 0 <= nc < m):
                return True
            
            if not visited[nr][nc] and storage[nr][nc] == "":
                visited[nr][nc] = True
                stack.append((nr, nc))
    return False