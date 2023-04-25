# 백준 2446. 별 찍기 - 9

N = int(input())

for i in range(N):
    print(' ' * i + '*' * (2 * (N - i) - 1))

for i in range(1, N):
    print(' ' * (N - 1 - i) + '*' * (2 * i + 1))