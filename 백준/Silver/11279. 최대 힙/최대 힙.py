# 백준 11279. 최대 힙
# heapq 모듈로 구현

import sys
import heapq
input = sys.stdin.readline

max_heap = []       # -를 붙여 최소 힙에 넣고 pop할 때 -를 붙여 출력하면 최댓값

N = int(input())
for tc in range(N):
    x = int(input())

    if x:   # x가 자연수이면 배열에 -x 삽입
        heapq.heappush(max_heap, -x)
    else:   # x가 0이면
        if max_heap:    # 배열이 비어있지 않으면
            print(-heapq.heappop(max_heap))     # 힙의 루트노드 값을 - 붙여서 pop
        else:           # 배열이 비어있으면
            print(0)