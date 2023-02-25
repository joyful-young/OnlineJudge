# 백준 1927. 최소 힙
# heapq 모듈로 구현

import sys
import heapq
input = sys.stdin.readline

heap = []

N = int(input())
for _ in range(N):
    x = int(input())

    if x:   # x가 자연수이면 배열에 x 삽입
        heapq.heappush(heap, x)
    else:       # x가 0이면
        if heap:    # 배열이 비어있지 않으면
            print(heapq.heappop(heap))
        else:       # 배열이 비었으면
            print(0)