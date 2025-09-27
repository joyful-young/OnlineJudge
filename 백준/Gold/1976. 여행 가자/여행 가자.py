# 1976. 여행 가자
import sys
input = sys.stdin.readline


def find(x):
    if rep[x] == x:
        return x

    rep[x] = find(rep[x])
    return rep[x]


def union(x, y):
    rep_x, rep_y = find(x), find(y)
    if rep_x != rep_y:
        rep[rep_y] = rep_x
    else:
        rep[rep_x] = rep_y


N = int(input())
M = int(input())
rep = [i for i in range(N + 1)]
for i in range(1, N + 1):
    arr = [0] + list(map(int, input().split()))
    for j in range(1, N + 1):
        if arr[j] == 1:
            union(i, j)

plan = list(map(int, input().split()))
start_rep = find(plan[0])
for i in range(1, M):
    if find(plan[i]) != start_rep:
        print("NO")
        break
else:
    print("YES")
