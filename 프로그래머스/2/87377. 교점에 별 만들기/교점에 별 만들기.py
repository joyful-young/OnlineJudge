def solution(line):
    N = len(line)
    
    # 정수 교점 좌표 구하기
    points = set()
    for i, j in comb(N):
        a, b, e = line[i]
        c, d, f = line[j]
        
        divisor = a * d - b * c
        if divisor == 0:
            continue
        
        x, xr = divmod(b * f - e * d, divisor)
        y, yr = divmod(e * c - a * f, divisor)
        
        if xr == 0 and yr == 0:
            points.add((y, x))
    
    # 교점이 하나 이상 존재하는 입력만 주어짐
    return draw(list(points))


def comb(n):
    combinations = []
    
    c = [0, 0]
    def recur(r, s):
        if r == 0:
            combinations.append(tuple(c))
            return
        
        
        for i in range(s, n - r + 1):
            c[r - 1] = i
            recur(r - 1, i + 1)
    
    recur(2, 0)
    return combinations


def draw(points):
    min_r, min_c = points[0]
    max_r, max_c = points[0]
    
    for r, c in points:
        min_r = min(min_r, r)
        max_r = max(max_r, r)
        min_c = min(min_c, c)
        max_c = max(max_c, c)
    
    n = max_r - min_r + 1
    m = max_c - min_c + 1
    
    stars = [["." for _ in range(m)] for _ in range(n)]
    for r, c in points:
        stars[r - min_r][c - min_c] = "*"
        
    return ["".join(row) for row in stars[::-1]]
