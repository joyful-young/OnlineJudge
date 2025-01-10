def solution(board, skills):
    def use_skill(ty, r1, c1, r2, c2, degree):
        if ty == 1:
            degree *= -1
        arr[r1 + 1][c1 + 1] += degree
        if r2 + 1 < N:
            arr[r2 + 2][c1 + 1] -= degree
            if c2 + 1 < M:
                arr[r2 + 2][c2 + 2] += degree
        if c2 + 1 < M:
            arr[r1 + 1][c2 + 2] -= degree
            
            
    N, M = len(board), len(board[0])
    arr = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
            
    for skill in skills:
        use_skill(*skill)
    
    for j in range(1, M + 1):
        for i in range(1, N + 1):
            if j < M:
                arr[i][j + 1] += arr[i][j]
            arr[i][j] += arr[i - 1][j]
    
    answer = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] + arr[i + 1][j + 1] > 0:
                answer += 1
    return answer