dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solution(land):
    n, m = len(land), len(land[0])
    
    def dfs(r, c, label):
        land[i][j] = label
        stack = [(r, c)]
        cnt = 0
        while stack:
            r, c = stack.pop()
            cnt += 1
            
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < n and 0 <= nc < m and land[nr][nc] == 1:
                    land[nr][nc] = label
                    stack.append((nr, nc))
        return cnt
    
    # 석유 덩어리 라벨링
    label = 2
    oil = {}    # {석유 덩어리 라벨: 석유량}
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                oil[label] = dfs(i, j, label)
                label += 1
    
    # 각 열에서 뽑을 수 있는 석유량
    answer = 0
    for j in range(m):
        label_set = set()
        for i in range(n):
            if land[i][j] > 1:
                label_set.add(land[i][j])
        
        answer = max(answer, sum(oil[x] for x in label_set))
        
    return answer