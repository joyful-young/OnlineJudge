# 1368. 물대기
import sys
import heapq
input = sys.stdin.readline

def find(x):
    if rep[x] == x:
        return x
    
    rep[x] = find(rep[x])
    return rep[x]


def union(x, y):
    rep_x, rep_y = find(x), find(y)

    if rep_x <= rep_y:
        rep[rep_y] = rep_x
    else:
        rep[rep_x] = rep_y


N = int(input())
W = [0] + [int(input()) for _ in range(N)]
arr = [W] + [[W[i]] for i in range(1, N + 1)]   # arr[0][i]는 i번 우물을 파는 데 드는 비용
for i in range(1, N + 1):
    arr[i] += list(map(int, input().split()))

edges = []
for i in range(N):
    for j in range(i + 1, N + 1):
        heapq.heappush(edges, [arr[i][j], i, j])    # i, j를 잇는 간선. 비용 적은 순

rep = [i for i in range(N + 1)]

total_cost = 0
while edges:
    cost, node_x, node_y = heapq.heappop(edges)
    if find(node_x) != find(node_y):    # 사이클이 안 생기면 그 간선으로 잇는다
        union(node_x, node_y)
        total_cost += cost
print(total_cost)

