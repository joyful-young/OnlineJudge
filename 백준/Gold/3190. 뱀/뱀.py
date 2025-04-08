import sys
from collections import deque
input = sys.stdin.readline

di = [-1, 0, 1, 0]    # 상, 우, 하, 좌
dj = [0, 1, 0, -1]


N = int(input())
K = int(input())
apples = set()
for _ in range(K):
    r, c = map(int, input().split())
    apples.add((r - 1, c - 1))
    
L = int(input())

d = 1    # 오른쪽 방향
now = 0  # 현재 시각
snake = deque([(0, 0)])
for i in range(L):
    # s: 방향 바뀔 시간, r: 회전 방향
    s, r = input().split()
    s = int(s)

    # (s - now)초를 현재의 방향으로 직진할 수 있는지
    can_move = True
    while now < s:
        now += 1
        # 머리를 다음 칸으로
        head = (snake[0][0] + di[d], snake[0][1] + dj[d])

        # 벽이나 몸과 부딪히면 게임 끝
        if (not (0 <= head[0] < N and 0 <= head[1] < N)) or head in snake:
            can_move = False
            break

        snake.appendleft(head)
        if head in apples:
            # 사과 먹고 몸 늘이기
            apples.remove(head)
        else:
            # 꼬리칸 비우기
            snake.pop()

    if can_move:
        if r == "L":
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
    else:
        print(now)
        break
else:
    while True:
        now += 1
        head = (snake[0][0] + di[d], snake[0][1] + dj[d])
        
        # 벽이나 몸과 부딪히면 게임 끝
        if (not (0 <= head[0] < N and 0 <= head[1] < N)) or head in snake:
            print(now)
            break

        snake.appendleft(head)
        if head in apples:
            # 사과 먹고 몸 늘이기
            apples.remove(head)
        else:
            # 꼬리칸 비우기
            snake.pop()