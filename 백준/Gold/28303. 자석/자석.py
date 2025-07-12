import sys
input = sys.stdin.readline


N, K = map(int, input().split())
energy_const = list(map(int, input().split()))

# N극이 S극보다 오른쪽
max_diff = -2 * N * K
min_s = energy_const[0]
for n in range(1, N):
    current_n = energy_const[n] - n * K
    max_diff = max(current_n - min_s, max_diff)
    min_s = min(current_n, min_s)

# N극이 S극보다 왼쪽
min_s = energy_const[-1] + (N - 1) * K
for n in range(N - 2, -1, -1):
    current_n = energy_const[n] + n * K
    max_diff = max(current_n - min_s, max_diff)
    min_s = min(current_n, min_s)

print(max_diff)
