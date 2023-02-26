# 백준 2075. N번째 큰 수

import sys
import heapq
input = sys.stdin.readline

N = int(input())

heap = []

for i in range(N):
    arr = list(map(int, input().split()))

    for num in arr:
        if len(heap) < N:       # 최대 N개까지만 들어가도록
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:   # 루트 노드에 있는 값보다 큰 값일 경우
                heapq.heappushpop(heap, num)    # 넣고 최솟값 빼냄

print(heap[0])  # N번째 큰 수