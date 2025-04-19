import sys
input = sys.stdin.readline

def find(x):
    if rep[x] == x:
        return x

    rep[x] = find(rep[x])
    return rep[x]

def union(x, y):
    rep_x = find(x)
    rep_y = find(y)

    if rep_x <= rep_y:
        rep[rep_y] = rep_x
    else:
        rep[rep_x] = rep_y


N, M = map(int, input().split())
rep = [i for i in range(N)]

for i in range(1, M + 1):
    x, y = map(int, input().split())

    if find(x) == find(y):
        print(i)
        break

    union(x, y)
else:
    print(0)