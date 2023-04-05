# 백준 4386. 별자리 만들기
import sys
from math import sqrt
input = sys.stdin.readline


n = int(input())
stars = [0] * n
INF = 1e6
dist = [[INF for _ in range(n)] for _ in range(n)]      # 별들 간의 거리
for i in range(n):
    dist[i][i] = 0      # 자기 자신과의 거리는 0

for i in range(n):      # 별들 좌표 입력받기
    x, y = map(float, input().split())
    stars[i] = (x, y)   # 리스트에 저장

MST = [0]           # 별자리(MST)에 포함되었는지. 0번 별 선택
ans = 0
for _ in range(n - 1):      # 0번을 제외하고 나머지 별들 선택
    tmp = INF               # MST에 있는 별과 최소 거리에 있는 별 찾기
    tmp_idx = 0
    tmp_star = 0
    # print(MST)
    for star in MST:        # MST에 포함된 별에 대해
        si, sj = stars[star]    # MST에 포함된 한 별의 좌표
        # print('mst', si, sj)
        for i in range(n):      # 다른 별들 중 거리 제일 가까운 것 찾기
            # if i in MST:        # 이미 포함된 별이면 넘어감
            #     continue
            if i not in MST:        # 아직 트리에 들어가지 않은 별
                ti, tj = stars[i]   # 좌표 가져오기
                # print('아직 아닌', ti, tj)

                if dist[star][i] == INF:    # 구해보지 않은 거리이면
                    dist[star][i] = dist[i][star] = sqrt((ti - si) ** 2 + (tj - sj) ** 2)   # 계산된 적 없으면 계산해서 넣기
                    # print('안구해봤어', star, i, dist[star][i])

                if tmp > dist[star][i]:     # 거리 더 작은 별이면 갱신
                    tmp = dist[star][i]
                    tmp_idx = i
                    tmp_star = star
                    # print('갱신됐어', dist[star][i], i)
    # MST에 속한 별과 가장 가까운 별의 거리와 인덱스를 구함
    # print(dist[tmp_star][tmp_idx], tmp_idx)
    MST.append(tmp_idx)     # 그 별 MST에 속하게
    ans += dist[tmp_star][tmp_idx]      # 비용에 더하기
# print(MST)
# print(dist)
print(ans)