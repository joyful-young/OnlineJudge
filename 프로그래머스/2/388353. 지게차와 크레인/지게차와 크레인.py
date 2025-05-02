dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    storage = [list(storage[i]) for i in range(n)]
    loads = {}
    for i in range(n):
        for j in range(m):
            if storage[i][j] in loads:
                loads[storage[i][j]].append((i, j))
            else:
                loads[storage[i][j]] = [(i, j)]
    
    for request in requests:
        if request[0] not in loads:
            continue
        
        if len(request) == 2:
            # 접근 가능 여부 상관 없이 모든 짐 출고
            for r, c in loads[request[0]]:
                storage[r][c] = ""
            del loads[request[0]]
        else:
            # 접근 가능한 짐만 출고
            remains = remove_accessible_loads(loads[request], storage)
            if not remains:
                del loads[request]
            else:
                loads[request] = remains
    
    return sum(len(loads_lst) for loads_lst in loads.values())


def remove_accessible_loads(loads_lst, cur_storage):
    n = len(loads_lst)
    is_removed = [False for _ in range(n)]
    for i in range(n):
        r, c = loads_lst[i]
        if is_accessible(r, c, cur_storage):
            is_removed[i] = True
    
    for i in range(n):
        if is_removed[i]:
            cur_storage[loads_lst[i][0]][loads_lst[i][1]] = ""
    
    return [loads_lst[i] for i in range(n) if not is_removed[i]]    # 출고 후 남은 짐


def is_accessible(sr, sc, cur_storage):
    n, m = len(cur_storage), len(cur_storage[0])
    stk = [(sr, sc)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    while stk:
        r, c = stk.pop()
        
        if visited[r][c]:
            continue
        
        visited[r][c] = True
        
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if not (0 <= nr < n and 0 <= nc < m):
                return True
            
            if not cur_storage[nr][nc] and not visited[nr][nc]:     # 빈 문자열일 경우
                stk.append((nr, nc))
    return False