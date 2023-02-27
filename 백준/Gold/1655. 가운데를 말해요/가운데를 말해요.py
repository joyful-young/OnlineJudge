# 백준 1655. 가운데를 말해요

import sys
import heapq
input = sys.stdin.readline

N = int(input())

max_heap = []   # 왼쪽    # 루트노드에 있는 것이 중간값이 되도록
min_heap = []   # 오른쪽

for _ in range(N):
    tmp = int(input())
    if len(max_heap) == len(min_heap):      # 양쪽에 똑같이 들어있으면 왼쪽에 넣어야.
        if min_heap and tmp > min_heap[0]:      # 오른쪽 최솟값보다 큰 수이면
            heapq.heappush(max_heap, -heapq.heappop(min_heap))  # 오른쪽 최솟값 빼다가 왼쪽에 넣고
            heapq.heappush(min_heap, tmp)       # 오른쪽에 tmp 넣기
        else:       # 오른쪽 최솟값보다 크지 않으면
            heapq.heappush(max_heap, -tmp)      # 왼쪽에 넣기
    else:       # 왼쪽에 더 많이 들어있을 때는 오른쪽에 넣어야
        if max_heap and -max_heap[0] > tmp:     # 왼쪽 최댓값보다 tmp가 더 작은 값이면 왼쪽에 넣어야.
            heapq.heappush(min_heap, -heapq.heappop(max_heap))  # 왼쪽 최댓값 빼다가 오른쪽에 넣고
            heapq.heappush(max_heap, -tmp)      # 왼쪽에 tmp 넣기
        else:       # tmp가 왼쪽 최댓값 이상이면 오른쪽에 넣으면 됨
            heapq.heappush(min_heap, tmp)

    print(-max_heap[0])