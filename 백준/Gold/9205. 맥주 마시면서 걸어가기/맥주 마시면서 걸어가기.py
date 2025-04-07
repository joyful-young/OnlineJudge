import sys
from collections import deque
input = sys.stdin.readline

DIST = 20 * 50

def get_dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def bfs(home, cs, goal):
    # 맥주 20개 있을 때, 다음 편의점을 1000m 안에 가면 됨

    # 도착지에 바로 갈 수 있을 경우
    if get_dist(home, goal) <= DIST:
        return "happy"

        
    # 편의점별 방문 여부
    store_cnt = len(cs)
    visited = [0 for _ in range(store_cnt)]
    q = deque([home])

    while q:
        v = q.popleft()

        if get_dist(v, goal) <= DIST:
            return "happy"

        for i in range(store_cnt):
            if visited[i] == 0 and get_dist(v, cs[i]) <= DIST:
                q.append(cs[i])
                visited[i] = 1
    return "sad"

T = int(input())
for _ in range(T):
    N = int(input())
    home = tuple(map(int, input().split()))
    stores = [tuple(map(int, input().split())) for _ in range(N)]
    goal = tuple(map(int, input().split()))

    print(bfs(home, stores, goal))
    