def solution(begin, end):
    answer = [1 for _ in range(end - begin + 1)]
    
    for i in range(len(answer)):
        number = i + begin
        if number == 1:
            answer[i] = 0
            continue
        
        sqrt_n = number ** 0.5
        for x in range(2, int(sqrt_n) + 1):
            q, r = divmod(number, x)
            if r == 0 and q <= 10000000:
                answer[i] = q
                break
            elif r == 0:
                answer[i] = x
        
    return answer

