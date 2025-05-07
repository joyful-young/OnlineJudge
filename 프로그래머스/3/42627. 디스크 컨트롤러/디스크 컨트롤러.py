from collections import deque
from heapq import heappush, heappop


def solution(jobs):
    N = len(jobs)
    jobs = [(jobs[i][1], jobs[i][0], i) for i in range(N)]  # (소요시간, 요청 시각, 작업 번호)
    jobs.sort(key=lambda x: x[1])       # 요청 시각 빠른 순
    dq = deque(jobs)
    
    turn_around = [0 for _ in range(N)]
    
    time = 0
    hq = []
    while True:
        
        # 특정 시점에서 요청되어있는 작업들 hq에 넣기
        while dq and dq[0][1] <= time:
            heappush(hq, dq.popleft())
        
        if hq:
            # 우선순위 가장 높은 것 처리
            l, s, x = heappop(hq)

            time += l
            turn_around[x] = time - s
        else:
            if dq:
                time = dq[0][1]
            else:
                break
        
    return sum(turn_around) // N