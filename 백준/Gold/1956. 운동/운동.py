import sys
input = sys.stdin.readline


INF = float('inf')
V, E = map(int, input().split())
adjM = [[INF if i != j else 0 for j in range(V + 1)] for i in range(V + 1)]

for _ in range(E):
    # 일방통행
    a, b, c = map(int, input().split())
    adjM[a][b] = c

# i -> k -> j
for k in range(1, V + 1):
    for i in range(1, V + 1):
        if adjM[i][k] == INF:
            continue
            
        for j in range(1, V + 1):
            d = adjM[i][k] + adjM[k][j]
            if d < adjM[i][j]:
                adjM[i][j] = d

answer = INF
for i in range(1, V + 1):
    for j in range(1, V + 1):
        if i != j and adjM[i][j] != INF and adjM[j][i] != INF:
            answer = min(answer, adjM[i][j] + adjM[j][i])
print(answer if answer != INF else -1)