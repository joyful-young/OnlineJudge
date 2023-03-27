# 백준 11723. 집합
import sys
input = sys.stdin.readline

M = int(input())
S = 0
for _ in range(M):
    op, *x = input().rstrip().split()
    if x:
        x = int(*x)
    if op == 'add':     # x 추가. 있으면 무시. 무조건 1로
        S = S | (1 << x)
    elif op == 'remove':    # x 제거. 없으면 무시. 무조건 0으로
        S = S & ~(1 << x)
    elif op == 'check':     # 있으면 1, 없으면 0
        if S & (1 << x):
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        S = S ^ (1 << x)
    elif op == 'all':
        S = 0b111111111111111111110
    else:
        S = 0

