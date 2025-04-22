def solution(arr):
    prime_numbers_under100 = prime_numbers(100)
    prime_dict = {k: 0 for k in prime_numbers_under100}
    
    for num in arr:
        if num == 1:
            continue
        
        prime_idx = 0
        temp_prime_dict = {k: 0 for k in prime_numbers_under100}
        while num > 1:
            if num % prime_numbers_under100[prime_idx] == 0:
                num //= prime_numbers_under100[prime_idx]
                temp_prime_dict[prime_numbers_under100[prime_idx]] += 1
            else:
                prime_idx += 1
        
        for k in prime_dict:
            prime_dict[k] = max(prime_dict[k], temp_prime_dict[k])
    
    answer = 1
    for k, v in prime_dict.items():
        answer *= (k ** v)
    return answer


def is_prime(number):
    # number 2 이상일 때 소수 판별
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def prime_numbers(max_number):
    # max_number 이하의 소수 목록 반환
    prime = [True for _ in range(max_number + 1)]
    prime[0] = False
    prime[1] = False
    
    for i in range(2, max_number + 1):
        if not prime[i]:
            continue
        
        if is_prime(i):
            num = i + i
            while num <= max_number:
                prime[num] = False
                num += i
    return tuple(i for i in range(2, max_number + 1) if prime[i])