# 백준 4485. 녹색 옷 입은 애가 젤다지?
import sys
import heapq
input = sys.stdin.readline

delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]

INF = 9 * 125 ** 2
case = 1
while True:
    N = int(input())
    if N == 0:
        break
    else:
        arr = [list(map(int, input().split())) for _ in range(N)]

        rupee = [[INF for _ in range(N)] for _ in range(N)]

        rupee[0][0] = arr[0][0]
        q = []
        heapq.heappush(q, (rupee[0][0], 0, 0))   # 시작점에서의 최소비용, 좌표
        while q:
            cost, ni, nj = heapq.heappop(q)     # 시작점에서부터의 비용이 최소인 지점

            if rupee[ni][nj] < cost:
                continue

            for di, dj in delta:
                ti, tj = ni + di, nj + dj
                if 0 <= ti < N and 0 <= tj < N:
                    tmp = cost + arr[ti][tj]
                    if tmp < rupee[ti][tj]:
                        rupee[ti][tj] = tmp
                        heapq.heappush(q, (tmp, ti, tj))
                        
        print(f'Problem {case}: {rupee[N - 1][N - 1]}')
        case += 1