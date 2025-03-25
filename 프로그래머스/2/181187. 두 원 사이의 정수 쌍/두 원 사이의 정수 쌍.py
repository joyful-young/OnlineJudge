def solution(r1, r2):
    answer = 0
    for x in range(0, r2):
        temp = max(0, r1 * r1 - x * x) ** 0.5
        min_y = max(1, int(temp)) if int(temp) == temp else int(temp) + 1
        
        max_y = int((r2 * r2 - x * x) ** 0.5)
        answer += max_y - min_y + 1
    return answer * 4