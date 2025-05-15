from heapq import heappush, heappop


def solution(operations):
    deleted = set()
    min_heap = []
    max_heap = []
    for i, oper in enumerate(operations):
        c, n = oper.split()
        n = int(n)
        
        if c == "I":
            # 큐에 삽입
            heappush(min_heap, (n, i))
            heappush(max_heap, (-n, i))
            continue

        if n == 1:
            # 최댓값 삭제
            maximum = get_max(max_heap, deleted)
            
            if maximum:
                deleted.add(maximum[1])
        else:
            # 최솟값 삭제
            minimum = get_min(min_heap, deleted)
            
            if minimum:
                deleted.add(minimum[1])
    
    minimum = get_min(min_heap, deleted)
    if not minimum:
        return [0, 0]
    
    deleted.add(minimum[1])
    maximum = get_max(max_heap, deleted)
    if not maximum:
        return [minimum[0], minimum[0]]
    
    return [-maximum[0], minimum[0]]


def get_min(min_h, deleted):
    while min_h and min_h[0][1] in deleted:
        heappop(min_h)
    return heappop(min_h) if min_h else None


def get_max(max_h, deleted):
    while max_h and max_h[0][1] in deleted:
        heappop(max_h)
    return heappop(max_h) if max_h else None