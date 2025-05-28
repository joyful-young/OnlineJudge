import sys
input = sys.stdin.readline


def find(x):
    if rep[x] == x:
        return x

    rep[x] = find(rep[x])
    return rep[x]


def union(x, y):
    rep_x, rep_y = find(x), find(y)

    if rep_x < rep_y:
        rep[rep_y] = rep_x
    else:
        rep[rep_x] = rep_y


N, M = map(int, input().split())
knowing = list(map(int, input().split()))
parties = [list(map(int, input().split())) for _ in range(M)]


if knowing[0] == 0:
    print(M)
else:
    rep = [i for i in range(N + 1)]

    for i in range(M):
        if parties[i][0] <= 1:
            continue

        for j in range(1, parties[i][0]):
            for k in range(j + 1, parties[i][0] + 1):
                union(parties[i][j], parties[i][k])

    group = set(find(i) for i in knowing[1:])
    ans = 0
    for party in parties:
        for person in party[1:]:
            if find(person) in group:
                break
        else:
            ans += 1
    print(ans)