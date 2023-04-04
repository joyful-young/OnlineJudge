# 백준 9372. 상근이의 여행
import sys
input = sys.stdin.readline


def find_set(x):
    while rep[x] != x:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    graph = []              # 그래프 저장
    for _ in range(M):
        a, b = map(int, input().split())
        graph.append([a, b])
        graph.append([b, a])    # 왕복

    # 신장 트리 만들기 - N개 국가 연결
    rep = [i for i in range(N + 1)]     # make-set
    cnt = 0     # 간선의 수. 비행기 종류의 수

    for u, v in graph:
        if find_set(u) != find_set(v):      # 사이클이 생기지 않으면
            cnt += 1
            union(u, v)     # 집합 합치기
            for i in range(2, N + 1):
                if find_set(i) != find_set(1):      # 대표원소가 모두 같지 않으면(모두 같은 집합에 속하지 않았으면)
                    break       # 더 연결해야 함
            else:       # 모두 같은 집합에 속했으면 완성된 것
                break
    print(cnt)