# 백준 13335. 트럭
from collections import deque

n, w, L = map(int, input().split())
arr = deque(list(map(int, input().split())))

q = deque([0] * w)     # 다리 위 공간
time = 0
# print(q)

while q:
    time += 1
    q.popleft()

    if arr:     # 트럭 남아있으면
        if sum(q) + arr[0] <= L:    # 다음 트럭이 들어와도 최대하중 넘지 않으면 트럭 들어옴
            q.append(arr.popleft())
        else:
            q.append(0)         # 최대하중 넘으면 빈자리 추가
    # 트럭 더 없으면 마지막 트럭이 완전히 빠져나갈때까지 while문 반복

print(time)