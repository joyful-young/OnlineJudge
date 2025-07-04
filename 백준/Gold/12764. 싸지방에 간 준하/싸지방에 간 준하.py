import sys
from heapq import heappush, heappop
input = sys.stdin.readline


N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]
people.sort()

pq = []
heappush(pq, (people[0][1], 0))
computers = [1]
empty_computers = []
for s, e in people[1:]:
    # 해당 시점에 비어있는 컴퓨터 구하기
    while pq and pq[0][0] <= s:
        heappush(empty_computers, heappop(pq)[1])

    if empty_computers:
        # 빈 자리 있을 경우 가장 작은 번호로
        idx = heappop(empty_computers)
        computers[idx] += 1
        heappush(pq, (e, idx))
    else:
        # 빈 자리 없으면 새 컴퓨터 자리 추가
        computers.append(1)
        heappush(pq, (e, len(computers) - 1))

print(len(computers))
print(*computers)