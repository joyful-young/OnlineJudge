# 백준 2441. 별 찍기 - 4
N = int(input())
n = N
while n > 0:
    for i in range(N - n):
        print(' ', end='')
    for i in range(n):
        print('*', end='')
    n -= 1
    print()
