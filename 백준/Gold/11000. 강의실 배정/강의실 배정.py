# 백준 11000. 강의실 배정 - 우선순위큐 이용

import sys
import heapq
input = sys.stdin.readline

N = int(input())

arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort()      # 강의 시작시간 기준으로 정렬

heap = []       # 다른 강의실에서 할 수업들
heapq.heappush(heap, arr[0][1])     # 강의 시작 시간이 가장 빠른 강의의 종료 시간 push

for i in range(1, N):       # arr의 인덱스 1 ~ (N - 1)
    if arr[i][0] < heap[0]:        # 현재 진행중인 강의들 중 종료 시간이 가장 빠른 강의가 끝나기 전에 시작한다면
        heapq.heappush(heap, arr[i][1])     # 그 강의의 종료시간 push. 새로운 강의실
    else:               # 현재 진행 중인 강의 중 제일 빨리 끝나는 강의 후에 이어서 진행 가능하다면
        heapq.heappop(heap)     # 진행 중이던 강의 종료하고
        heapq.heappush(heap, arr[i][1])     # 그 강의실에서 이어서 시작하는 걸로 생각

# arr의 모든 원소를 확인하고 나면 우선순위큐에 남아있는 수업의 수는 필요한 강의실의 수
print(len(heap))