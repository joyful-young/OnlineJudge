# 백준 9372. 상근이의 여행
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    
    for _ in range(M):
        a, b = map(int, input().split())
    
    print(N - 1)
