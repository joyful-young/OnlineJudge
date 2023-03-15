# 백준 12851. 숨바꼭질2

from collections import deque

N, K = map(int, input().split())

queue = deque()
queue.append(N)

visited = [0 for _ in range(100001)]
ans_way = 0
ans_cnt = 0
while queue:
    t = queue.popleft()     # 현재 위치
    cnt = visited[t]        # 여기까지 오는 데 걸린 시간

    if t == K:      # 동생이 있는 곳이면
        # ans_cnt = cnt
        # ans_way += 1
        # continue
        ans_cnt = cnt       # 최단시간
        # print(queue)
        ans_way = queue.count(K) + 1        # ans_cnt 초에 K에 도달한 것들의 수(앞에서 하나 뺐기 때문에 다시 더해줌)
        break

    for n in [t - 1, t + 1, 2 * t]:
        # 범위 내. 방문한 적 없거나 같은 시간대에 방문하는 곳이면
        if 0 <= n <= 100000 and (visited[n] == 0 or visited[n] == visited[t] + 1):
            queue.append(n)
            visited[n] = visited[t] + 1

print(ans_cnt)
print(ans_way)
