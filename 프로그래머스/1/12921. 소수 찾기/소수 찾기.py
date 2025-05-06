def solution(n):
    numbers = [True for i in range(1, n + 1)]
    for num in range(1, n + 1):
        if not numbers[num - 1]:
            continue
            
        if is_prime(num):
            num += num
            while num <= n:
                numbers[num - 1] = False
                num += num
        else:
            numbers[num - 1] = False
    return numbers.count(True)


def is_prime(num):
    if num <= 1:
        return False
    
    for x in range(2, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True