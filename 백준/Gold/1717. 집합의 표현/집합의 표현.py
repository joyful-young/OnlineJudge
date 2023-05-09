# 백준 1717. 집합의 표현
import sys
input = sys.stdin.readline


def find_set(x):
    # while rep[x] != x:
    #     x = rep[x]
    # return x
    
    # 경로압축?
    if rep[x] != x:
        rep[x] = find_set(rep[x])
    return rep[x]


def union(x, y):
    rep[find_set(y)] = find_set(x)


n, m = map(int, input().split())

# make_set
rep = [i for i in range(n + 1)]
for _ in range(m):
    op, a, b = map(int, input().split())

    if op == 0:
        union(a, b)
    else:
        if find_set(a) == find_set(b):
            print('YES')
        else:
            print('NO')
