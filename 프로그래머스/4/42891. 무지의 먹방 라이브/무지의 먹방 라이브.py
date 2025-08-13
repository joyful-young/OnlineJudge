from heapq import heappush, heappop


def solution(food_times, k):
    n = len(food_times)
    food_hq = []
    for idx in range(n):
        heappush(food_hq, (food_times[idx], idx + 1))    # (시간, 번호)
    
    now = 0
    prev = 0
    while food_hq:
        min_time = food_hq[0][0]
        now += (min_time - prev) * n
        prev = min_time
        if now >= k:
            remained_food = [food[1] for food in food_hq]
            remained_food.sort()
            return remained_food[k % n - 1]
        else:
            while food_hq and min_time == food_hq[0][0]:
                heappop(food_hq)
                n -= 1
    return -1


def solution(food_times, k):
    n = len(food_times)
    food_hq = []
    for idx in range(n):
        heappush(food_hq, (food_times[idx], idx + 1))    # (시간, 번호)

    passed_time = 0     # 지금까지 지난 시간
    prev = 0            # 이전에 먹은 음식에 필요했던 시간

    while food_hq:
        t = food_hq[0][0]
        need = (t - prev) * n
        
        if k < passed_time + need:
            remained = sorted(food[1] for food in food_hq)
            return remained[(k - passed_time) % n]
        
        passed_time += need
        prev = t

        # 이번에 다 먹은 음식들 제거
        while food_hq and food_hq[0][0] == t:
            heappop(food_hq)
            n -= 1

    return -1