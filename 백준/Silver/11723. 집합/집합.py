# 백준 11723. 집합
import sys
input = sys.stdin.readline

M = int(input())
S = set()
for _ in range(M):
    op, *x = input().rstrip().split()
    if x:
        x = int(*x)
    if op == 'add':
        S.add(x)
    elif op == 'remove':
        S.discard(x)
    elif op == 'check':
        if x in S:
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif op == 'all':
        S = set(range(1, 21))
    else:
        S.clear()

