from heapq import heapify, heappop, heappush

def solution(n, works):
    pq = [-w for w in works]
    heapify(pq)
    
    while n > 0:
        w = heappop(pq)
        if w == 0:
            return 0
        
        heappush(pq, w + 1)
        n -= 1
    
    return sum([w * w for w in pq])