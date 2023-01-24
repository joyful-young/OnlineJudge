# n 입력
n = int(input())

# 피보나치 수열
def fibonacci(n):
    # n = 0이면 0
    if n == 0:
        return 0
    # n = 1이면 1
    elif n == 1:
        return 1
    # 그밖엔 fibonacci(n) = fibonacci(n - 2) + fibonacci(n - 1)
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
# 출력
print(fibonacci(n))