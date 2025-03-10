def solution(num_list):
    cnt = 0
    for num in num_list:
        while num != 1:
            if num % 2:
                num = (num - 1) // 2
            else:
                num //= 2
            cnt += 1
    return cnt