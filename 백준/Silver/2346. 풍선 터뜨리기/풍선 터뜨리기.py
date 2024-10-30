# 2346. 풍선 터뜨리기
from collections import deque

N = int(input())
balloons = deque(list(zip(list(map(int, input().split())), [i for i in range(1, N + 1)])))
ans = []
while balloons:
    number, idx = balloons.popleft()
    ans.append(idx)
    if number > 0:
        balloons.rotate(-(number - 1))
    else:
        balloons.rotate(-number)

print(*ans)