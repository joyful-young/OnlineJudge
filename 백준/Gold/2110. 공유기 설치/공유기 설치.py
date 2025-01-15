# 2110. 공유기 설치
import sys
input = sys.stdin.readline


def count_router(distance):
    prep = houses[0]    # 바로 이전에 설치된 공유기 위치
    cnt = 1
    for x in houses[1:]:
        if x - prep >= distance:     # 이전 위치와 x와의 거리가 가장 인접한 거리 이상이면 x에 설치
            cnt += 1
            prep = x
    return cnt


def solution(l, r):
    max_adj_dist = 0
    while l <= r:
        mid = (l + r) // 2
        routers = count_router(mid)
        if routers >= C:
            max_adj_dist = mid
            l = mid + 1      # 더 먼 거리도 가능할 수 있음
        else:
            r = mid - 1
    return max_adj_dist


N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

left = 1
right = houses[-1] - houses[0]
print(solution(left, right))