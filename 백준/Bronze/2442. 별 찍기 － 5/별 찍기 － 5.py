# 백준 2442. 별 찍기 - 5
N = int(input())

for i in range(N):
    for _ in range(N - i - 1):
        print(' ', end='')

    for _ in range(2 * i + 1):
        print('*', end='')

    print()
