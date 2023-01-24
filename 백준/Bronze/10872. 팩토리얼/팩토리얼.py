# N 입력
N = int(input())

# N! = N * (N - 1)!
def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N - 1)

# 출력
print(factorial(N))