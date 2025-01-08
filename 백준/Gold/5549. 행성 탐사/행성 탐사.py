# 5549. 행성 탐사
import sys
input = sys.stdin.readline


def count(left_i, left_j, right_i, right_j, arr):
    return arr[right_i][right_j] - arr[right_i][left_j - 1] - arr[left_i - 1][right_j] + arr[left_i - 1][left_j - 1]


def get_answer(coordinates):
    left_i, left_j, right_i, right_j = coordinates
    return (count(left_i, left_j, right_i, right_j, jungle),
            count(left_i, left_j, right_i, right_j, ocean),
            count(left_i, left_j, right_i, right_j, ice))


M, N = map(int, input().split())    # 행, 열
K = int(input())

jungle = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
ocean = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
ice = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

# 지도 정보 입력 & 가로 방향 누적 합 계산
for i in range(1, M + 1):
    row = input().rstrip()
    for j in range(1, N + 1):
        if row[j - 1] == "J":
            jungle[i][j] = jungle[i][j - 1] + 1
            ocean[i][j] = ocean[i][j - 1]
            ice[i][j] = ice[i][j - 1]
        elif row[j - 1] == "O":
            ocean[i][j] = ocean[i][j - 1] + 1
            jungle[i][j] = jungle[i][j - 1]
            ice[i][j] = ice[i][j - 1]
        else:
            ice[i][j] = ice[i][j - 1] + 1
            jungle[i][j] = jungle[i][j - 1]
            ocean[i][j] = ocean[i][j - 1]
# 세로 방향 누적 합
for i in range(2, M + 1):
    for j in range(1, N + 1):
        jungle[i][j] += jungle[i - 1][j]
        ocean[i][j] += ocean[i - 1][j]
        ice[i][j] += ice[i - 1][j]

for _ in range(K):
    print(*get_answer(list(map(int, input().rstrip().split()))))