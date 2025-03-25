def solution(r1, r2):
    """
    1사분면(y축 포함, x축 제외)에서 점 개수 구해서 4배
    0 <= x < r2, 0 < y <= r2
    max(1, (r1)^2 - x^2) <= y^2 <= (r2)^2 - x^2
    """
    answer = 0
    for x in range(0, r2):
        temp = max(1, r1 * r1 - x * x) ** 0.5
        min_y = int(temp) if int(temp) == temp else int(temp) + 1
        
        max_y = int((r2 * r2 - x * x) ** 0.5)
        answer += max_y - min_y + 1
    return answer * 4