import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())


def count(a):
    if a <= B:
        return 1

    a -= B
    q, r = divmod(a, C)
    if r == 0:
        return q + 1
    return q + 2

cnt = 0
for a in A:
    cnt += count(a)
print(cnt)