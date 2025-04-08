import sys
from collections import deque
input = sys.stdin.readline


N, K = map(int, input().split())
A = deque(list(map(int, input().split())))    # 각 칸의 내구도
zero_durability = 0
for a in A:
    if a == 0:
        zero_durability += 1

belt_len = 2 * N
robots = deque([False for _ in range(belt_len)])    # 로봇 있는지

step = 1
while True:
    # 단계 진행
    # 1. 한 칸 회전 - 로봇 내리기
    A.rotate(1)
    robots.rotate(1)
    robots[N - 1] = False

    # 2. 로봇 이동
    for i in range(N - 2, -1, -1):
        if robots[i] and not robots[i + 1] and A[i + 1] > 0:
            robots[i] = False
            robots[i + 1] = True
            A[i + 1] -= 1
            if A[i + 1] == 0:
                zero_durability += 1
    robots[N - 1] = False    # 로봇 이동 후 내리는 위치 도착했을 때 바로 내림

    # 3. 로봇 올리기
    if A[0] > 0:
        robots[0] = True
        A[0] -= 1
        if A[0] == 0:
            zero_durability += 1

    # 4. 과정 더 진행할지 확인
    if zero_durability < K:
        step += 1
    else:
        break

print(step)