# 백준 15686. 치킨 배달
def nCr(n, r, s):
    global ans
    if r == 0:      # 다 뽑으면 도시의 치킨거리 계산
        d = 0
        for i in range(h):
            hi, hj = home[i]
            tmp = 100
            for ci, cj in comb:
                tmp = min(tmp, abs(hi - ci) + abs(hj - cj))
            d += tmp
        ans = min(ans, d)
    else:
        for j in range(s, n - r + 1):
            comb[r - 1] = chi[j]
            nCr(n, r - 1, j + 1)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

chi = []
home = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append((i, j))
        elif arr[i][j] == 2:
            chi.append((i, j))      # 치킨집 좌표 저장

# 조합
h = len(home)       # 전체 집의 수
total = len(chi)    # 전체 치킨집 수
comb = [0] * M      # 조합 저장할 배열
INF = 10000000
ans = INF
nCr(total, M, 0)    # 전체 중 아직 뽑아야 하는 게 M개 남았고 0번 인덱스부터 뽑기 가능
print(ans)