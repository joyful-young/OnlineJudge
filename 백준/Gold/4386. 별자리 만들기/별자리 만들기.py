# 백준 4386. 별자리 만들기
import sys
from math import sqrt
import heapq
input = sys.stdin.readline

# Prim 알고리즘
n = int(input())
stars = [0] * n
dist = [[0 for _ in range(n)] for _ in range(n)]      # 별들 간의 거리
for i in range(n):      # 별들 좌표 입력받기
    x, y = map(float, input().split())
    stars[i] = (x, y)   # 리스트에 저장

for i in range(n):              # i번 별과 j번 별 사이의 거리 미리 계산
    for j in range(n):
        dist[i][j] = sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2)

# [1] 임의의 정점에서 시작
MST = []
cand = []
heapq.heappush(cand, (0, 0))     # 별자리(MST)에 연결될 별 후보. (MST와의 최단거리, 별 번호)
ans = 0
while len(MST) < n:      # (n - 1)개 선택하면 MST 완성
    # [2] 최소 거리의 정점 선택
    min_d, star = heapq.heappop(cand)
    if star in MST:     # 이미 MST에 들어간 별이면 넘김
        continue
    MST.append(star)
    ans += min_d

    for i in range(n):      # 다른 별들 중 거리 제일 가까운 것 찾기
        if i not in MST:        # 아직 트리에 들어가지 않은 별
            heapq.heappush(cand, (dist[star][i], i))

print(ans)