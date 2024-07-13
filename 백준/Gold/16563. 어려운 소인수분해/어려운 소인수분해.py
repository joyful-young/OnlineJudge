# 16563. 어려운 소인수분해
import math

def prime_factorization(number):
    ans = []
    for prime_number in prime_numbers:
        if prime_number * prime_number > number:
            break
        while number % prime_number == 0:
            ans.append(prime_number)
            number //= prime_number
    if number > 1:
        ans.append(number)
    return ans


N = int(input())
numbers = list(map(int, input().split()))

# max_num = 5000000
max_num = max(numbers)

is_prime = [True for _ in range(max_num + 1)]     # 0 ~ N
for num in range(2, int(math.sqrt(max_num)) + 1):
    if is_prime[num]:
        x = num
        while num * x <= max_num:
            is_prime[num * x] = False
            x += 1

prime_numbers = [num for num in range(2, max_num + 1) if is_prime[num]]

for number in numbers:
    print(*prime_factorization(number))
