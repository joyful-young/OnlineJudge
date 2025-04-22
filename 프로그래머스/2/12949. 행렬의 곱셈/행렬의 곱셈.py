def solution(arr1, arr2):
    # c1 = r2
    r1 = len(arr1)
    c1 = len(arr1[0])
    c2 = len(arr2[0])
    
    answer = [[0 for _ in range(c2)] for _ in range(r1)]
    for r in range(r1):
        for c in range(c2):
            for i in range(c1):
                answer[r][c] += arr1[r][i] * arr2[i][c]
    return answer