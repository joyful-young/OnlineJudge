# 백준 12865. 평범한 배낭

import sys

N, K = map(int, sys.stdin.readline().split())

things = [[0, 0] for _ in range(N + 1)]

for i in range(1, N + 1):
    things[i] = list(map(int, sys.stdin.readline().split()))    # [무게, 가치]
# print(things)

D = [[0] * (K + 1) for _ in range(N + 1)]   # 행: 0 ~ N, 열: 0 ~ K

# D[i][j]: i번째 물건까지 봤을 때 무게가 j인 배낭의 최대 가치

for i in range(1, N + 1):
    for j in range(1, K + 1):
        W, V = things[i]        # i번째 물건의 무게와 가치
        if j < W:       # 허용 무게보다 많이 나가면 넣지 않는다
            D[i][j] = D[i - 1][j]
        else:           # 넣을 무게만큼 빼고 지금 걸 넣거나, 그냥 놔두거나
            D[i][j] = max(D[i - 1][j], D[i - 1][j - W] + V)

# print(D)
print(D[N][K])
