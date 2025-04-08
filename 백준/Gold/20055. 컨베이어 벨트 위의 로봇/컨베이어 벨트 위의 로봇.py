# 시간초과 코드
import sys
input = sys.stdin.readline


N, K = map(int, input().split())
A = list(map(int, input().split()))    # 각 칸의 내구도
zero_durability = 0
for a in A:
    if a == 0:
        zero_durability += 1

# 올리는 위치. up ~ up + (N - 1) 까지 로봇이 있을 수 있음
up = 0

belt_len = 2 * N
robots = [False for _ in range(belt_len)]    # 로봇 있는지
belt_idx = lambda x: x % belt_len

step = 1
while True:
    # 단계 진행
    # 1. 한 칸 회전 - 로봇 내리기
    up = belt_idx(up - 1)
    down = belt_idx(up + (N - 1))
    robots[down] = False

    # 2. 로봇 이동
    for i in range(N - 2, -1, -1):
        cur = belt_idx(up + i)
        nxt = belt_idx(cur + 1)
        if robots[cur] and not robots[nxt] and A[nxt] > 0:
            robots[cur] = False
            robots[nxt] = True
            A[nxt] -= 1
            if A[nxt] == 0:
                zero_durability += 1
    robots[down] = False    # 로봇 이동 후 내리는 위치 도착했을 때 바로 내림

    # 3. 로봇 올리기
    if A[up] > 0:
        robots[up] = True
        A[up] -= 1
        if A[up] == 0:
            zero_durability += 1

    # 4. 과정 더 진행할지 확인
    if zero_durability < K:
        step += 1
    else:
        break

print(step)