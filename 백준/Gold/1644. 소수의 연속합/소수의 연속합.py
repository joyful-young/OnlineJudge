N = int(input())


def get_prime_numbers(n):
    # N 이하의 소수 구하기
    if n == 1:
        return []
        
    is_prime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]

if N == 1:
    print(0)
else:
    answer = 0
    primes = get_prime_numbers(N)
    left = right = 0
    current_sum = 0

    while True:
        if current_sum >= N:
            if current_sum == N:
                answer += 1
            current_sum -= primes[left]
            left += 1
        elif right == len(primes):
            break
        else:
            current_sum += primes[right]
            right += 1

    print(answer)