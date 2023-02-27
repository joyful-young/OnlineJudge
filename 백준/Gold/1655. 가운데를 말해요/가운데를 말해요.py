# 백준 1655. 가운데를 말해요

import sys
import heapq
input = sys.stdin.readline

N = int(input())

max_heap = []   # 왼쪽    # 루트노드에 있는 것이 중간값이 되도록
min_heap = []   # 오른쪽

for _ in range(N):
    tmp = int(input())
    if len(max_heap) == len(min_heap):      # 양쪽에 똑같이 들어있으면 왼쪽에 넣기
        heapq.heappush(max_heap, -tmp)      # 최대힙이므로 - 붙여서 넣기

    else:                                   # 오른쪽이 더 적으면 오른쪽에 넣기
        heapq.heappush(min_heap, tmp)       # 최소힙

    if max_heap and min_heap and -max_heap[0] > min_heap[0]:     # 집어넣었을 때 왼쪽 힙 최댓값이 오른쪽 힙 최솟값보다 크면
        left = -heapq.heappop(max_heap)      # 왼쪽에서 빼냄
        right = heapq.heappop(min_heap)     # 오른쪽에서 빼냄
        heapq.heappush(max_heap, -right)
        heapq.heappush(min_heap, left)

    print(-max_heap[0])     # 왼쪽 힙의 루트 값이 중간값