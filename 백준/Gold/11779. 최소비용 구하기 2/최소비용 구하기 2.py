# 백준 11779. 최소비용 구하기2
import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]  # 도시 번호 1번 ~ n번
for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s].append((cost, e))    # 비용, 도착지 순으로 넣음

start, end = map(int, input().split())

INF = 1e9
min_cost = [[INF, []] for _ in range(n + 1)]
min_cost[start][0] = 0      # 출발지에서 출발지까지 비용은 0

q = []
heapq.heappush(q, (0, start))   # start까지의 최소비용, start
while q:
    now_cost, now = heapq.heappop(q)    # 현재 위치까지 최소비용이 가장 작은 곳의 최소비용, 현재 위치
    if min_cost[now][0] < now_cost:     # 이미 방문한 곳
        continue
    for cost, node in graph[now]:       # 현재 위치와 연결된 곳
        if min_cost[node][0] > now_cost + cost:  # 현재 위치를 거쳐서 가는 비용이 더 적으면 갱신할건데
            if min_cost[node][1]:       # 이전 위치 리스트가 비지 않았으면
                min_cost[node][0] = now_cost + cost     # 갱신하고
                min_cost[node][1].pop()     # 있던 거 빼고
                min_cost[node][1].append(now)   # 현재 위치 거쳐 간다고 표시
            else:           # 이전 위치 리스트 비었으면
                min_cost[node][0] = now_cost + cost
                min_cost[node][1].append(now)
            heapq.heappush(q, (min_cost[node][0], node))

print(min_cost[end][0])
# print(min_cost)

ans = [end]
tmp = end
while tmp != start:
    tmp = min_cost[tmp][1][0]
    ans.append(tmp)
print(len(ans))
print(*ans[::-1])