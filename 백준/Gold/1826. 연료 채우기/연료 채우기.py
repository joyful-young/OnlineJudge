# 1826. 연료 채우기
import sys
import heapq
input = sys.stdin.readline


N = int(input())
gas_stations = []
for _ in range(N):
    heapq.heappush(gas_stations, list(map(int, input().split())))   # 주유소 가까운 순으로

dist_to_vil, fuel_left = map(int, input().split())

heap = []   # 충전 가능 연료 기준 최대힙
cnt = 0

while fuel_left < dist_to_vil:
    while gas_stations and gas_stations[0][0] <= fuel_left: # 갈 수 있는 주유소들
        location, fuel = heapq.heappop(gas_stations)
        heapq.heappush(heap, [-fuel, location])
    
    if not heap:
        cnt = -1
        break

    fuel, location = heapq.heappop(heap)    # 갈 수 있는 주유소들 중 연료 가장 많이 넣을 수 있는 곳

    fuel_left -= fuel   # 힙에 음수로 들어있었음
    cnt += 1

print(cnt)
