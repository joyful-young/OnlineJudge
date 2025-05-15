import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def pop_invalid_v(hq, deleted):
    while hq and hq[0][1] in deleted:
        heappop(hq)


T = int(input())
for _ in range(T):
    k = int(input())

    deleted = set()
    min_heap = []
    max_heap = []
    for i in range(k):
        c, n = input().split()
        n = int(n)
        
        if c == "I":
            # 큐에 삽입
            heappush(min_heap, (n, i))
            heappush(max_heap, (-n, i))
            continue

        if n == 1:
            # 최댓값 삭제
            pop_invalid_v(max_heap, deleted)
            if max_heap:
                deleted.add(heappop(max_heap)[1])
        else:
            # 최솟값 삭제
            pop_invalid_v(min_heap, deleted)
            if min_heap:
                deleted.add(heappop(min_heap)[1])
                
    pop_invalid_v(min_heap, deleted)
    pop_invalid_v(max_heap, deleted)
    if not min_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])

