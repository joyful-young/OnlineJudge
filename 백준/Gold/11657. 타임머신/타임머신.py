import sys
input = sys.stdin.readline


INF = float('inf')
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# 1번부터 각 노드까지의 최단거리
dist = [INF] * (N + 1)
dist[1] = 0

# 벨만-포드 알고리즘
for _ in range(N - 1):
    for a, b, c in edges:
        if dist[a] != INF and dist[b] > dist[a] + c:
            dist[b] = dist[a] + c

# 음수 사이클 확인
is_updated = False
for a, b, c in edges:
    if dist[a] != INF and dist[b] > dist[a] + c:
        is_updated = True
        break

if is_updated:
    print(-1)
else:
    ans = [dist[i] if dist[i] != INF else -1 for i in range(2, N + 1)]
    print("\n".join(map(str, ans)))
    
