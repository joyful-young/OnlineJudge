import sys
input = sys.stdin.readline


N = int(input())
balls = []
for i in range(N):
    c, s = map(int, input().split())
    balls.append((s, c, i))

# 크기 오름차순 정렬
balls.sort(key=lambda x: x[0])

total_sum = 0
color_sum = [0] * (N + 1)
ans = [0] * N

j = 0
for i in range(N):
    si, ci, idx = balls[i]

    while balls[j][0] < si:
        sj, cj, _ = balls[j]
        # i보다 작은 공들의 크기 합
        total_sum += sj
        # i보다 작은 공들의 색별 크기 합
        color_sum[cj] += sj
        j += 1

    ans[idx] = total_sum - color_sum[ci]

print("\n".join(map(str, ans)))