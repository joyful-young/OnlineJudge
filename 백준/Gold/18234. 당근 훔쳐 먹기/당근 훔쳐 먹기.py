import sys
input = sys.stdin.readline

N, T = map(int, input().split())
# carrots[i] = (w, p)
carrots = [tuple(map(int, input().split())) for _ in range(N)]

# p 값이 큰 건 나중에 먹는 게 이득
# (p, w) 기준 내림차순
carrots.sort(key=lambda x: (x[1], x[0]), reverse=True)

answer = 0
for i in range(N):
    w, p = carrots[i]
    answer += w + (T - i - 1) * p

print(answer)