import sys
from heapq import heappush, heappop
input = sys.stdin.readline


N, K = map(int, input().split())

# 보석 (무게, 가격) 최소힙
gems = []
for _ in range(N):
    heappush(gems, tuple(map(int, input().split())))

# 가방. 담을 수 있는 무게 작은 것부터
bags = [int(input()) for _ in range(K)]
bags.sort()


# 현재 가방에 넣을 수 있는 보석들의 가치 최대힙
pending_gem_values = []
answer = 0
for max_weight in bags:
    # 가방에 담을 수 있는 것들 중 가치가 가장 큰 보석 구하기
    while gems and gems[0][0] <= max_weight:
        weight, value = heappop(gems)
        heappush(pending_gem_values, -value)

    if pending_gem_values:
        # 음수로 저장해두어서 빼야 함
        answer -= heappop(pending_gem_values)

print(answer)