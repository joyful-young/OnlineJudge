import sys
input = sys.stdin.readline


N = int(input())
balls = []
for i in range(N):
    c, s = map(int, input().split())
    balls.append((s, c, i))

# 크기 오름차순 정렬
balls.sort()

total_sum = 0
color_sum = [0] * (N + 1)
ans = [0] * N

j = 0
for i in range(N):
    si, ci, idx = balls[i]

    while balls[j][0] < si:
        sj, cj, _ = balls[j]
        total_sum += sj
        color_sum[cj] += sj
        j += 1

    ans[idx] = total_sum - color_sum[ci]

print("\n".join(map(str, ans)))