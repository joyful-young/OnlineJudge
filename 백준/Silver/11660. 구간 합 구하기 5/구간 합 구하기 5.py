# 백준 11660 구간 합 구하기 5

# 표의 크기 N, 합 구할 횟수 M
import sys

N, M = map(int, sys.stdin.readline().split())

# N X N 표
arr = [0] * N
for i in range(N):
    arr[i] = list(map(int, sys.stdin.readline().split()))

# 누적합 표
# 일단 가로줄로 누적. 첫번째 값은 0
row = [[0] for _ in range(N)]

for i in range(N):
    for j in range(N):
        row[i].append(row[i][j] + arr[i][j])

# 세로줄로도 누적
sum_arr = [[0] * (N + 1)]

for i in range(N):
    sum_arr.append([sum_arr[i][j] + row[i][j] for j in range(N + 1)])

# 좌표 입력 받아 답 출력
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    print(sum_arr[x2][y2] - sum_arr[x2][y1 - 1] - sum_arr[x1 - 1][y2] + sum_arr[x1 - 1][y1 - 1])
