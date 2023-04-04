# 백준 1197. 최소 스패닝 트리
import sys
input = sys.stdin.readline


def find_set(x):
    while rep[x] != x:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


V, E = map(int, input().split())
graph = []

for _ in range(E):
    A, B, C = map(int, input().split())
    graph.append([C, A, B])

graph.sort()

# make-set
rep = [i for i in range(V + 1)]     # 정점 번호 1 ~ V번

s = 0       # 가중치 합
cnt = 0
for c, a, b in graph:       # 가중치가 작은 것부터
    if find_set(a) != find_set(b):      # 사이클을 이루지 않으면
        s += c      # 가중치 더하고
        union(a, b)     # 두 집합 합치고
        cnt += 1        # 선택한 간선 수 증가

        if cnt == V - 1:        # 간선을 모두 선택. MST 완성
            break

print(s)