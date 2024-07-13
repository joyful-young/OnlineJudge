# 1202. 보석 도둑
import sys
import heapq
input = sys.stdin.readline


N, K = map(int, input().split())
jewels = []
for _ in range(N):
    heapq.heappush(jewels, list(map(int, input().split()))) # 보석 무게 작은 순

bags = [int(input()) for _ in range(K)]
bags.sort()     # 가방 담을 수 있는 최대 무게 작은 순으로

ans = 0
heap = []
for max_weight in bags: # 작은 가방부터 채우기
    while jewels and jewels[0][0] <= max_weight:
        w, v = heapq.heappop(jewels)
        heapq.heappush(heap, -v)    # 보석 가격 기준 최대힙
        
    if heap:
        ans -= heapq.heappop(heap)  # 가방에 넣을 수 있는 보석 중 가장 비싼 것
    elif not jewels:
        break

print(ans)
