# 백준 8901. 화학 제품

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())
    ab, bc, ca = map(int, input().split())

    maxV = 0
    for x in range(min(A, B) + 1):
        for y in range(min((B - x), C) + 1):
            tmp = ab * x + bc * y + ca * min(A - x, C - y)
            maxV = max(maxV, tmp)

    print(maxV)