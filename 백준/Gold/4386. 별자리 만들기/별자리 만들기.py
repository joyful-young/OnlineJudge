# 백준 4386. 별자리 만들기
import sys
from math import sqrt
input = sys.stdin.readline

# Prim 알고리즘
n = int(input())
stars = [0] * n
INF = 1e6
dist = [[INF for _ in range(n)] for _ in range(n)]      # 별들 간의 거리
for i in range(n):
    dist[i][i] = 0      # 자기 자신과의 거리는 0

for i in range(n):      # 별들 좌표 입력받기
    x, y = map(float, input().split())
    stars[i] = (x, y)   # 리스트에 저장

# [1] 임의의 정점에서 시작
MST = [0]           # 별자리(MST)에 포함된 별의 번호. 0번 별 선택
ans = 0
for _ in range(n - 1):      # 간선 (n - 1)개 선택하면 MST 완성
    tmp = INF               # MST에 있는 별과 최소 거리에 있는 별 찾기
    tmp_idx = 0             # MST와 새롭게 연결할 별
    mst_idx = 0             # 새롭게 연결되는 별과 연결될 MST의 별
    
    # [2] 최소 거리의 정점 선택
    for star in MST:        # MST에 포함된 별에 대해
        si, sj = stars[star]
        
        for i in range(n):      # 다른 별들 중 거리 제일 가까운 것 찾기
            if i not in MST:        # 아직 트리에 들어가지 않은 별
                ti, tj = stars[i]

                if dist[star][i] == INF:
                    dist[star][i] = dist[i][star] = sqrt((ti - si) ** 2 + (tj - sj) ** 2)   # 계산된 적 없으면 계산해서 넣기

                if tmp > dist[star][i]:     # 거리 더 작은 별이면 갱신
                    tmp = dist[star][i]
                    tmp_idx = i             # 연결되는 별
                    mst_idx = star          # 그 별과 연결될 MST의 별
    
    # MST에 속한 별 x MST에 속하지 않은 별 조합이 구해짐
    MST.append(tmp_idx)
    ans += dist[mst_idx][tmp_idx]      # 비용에 더하기
print(ans)