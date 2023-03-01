# 백준 1806. 부분합

N, S = map(int, input().split())

arr = list(map(int, input().split()))

prefix_sum = [0 for _ in range(N + 1)]      # 0번째 ~ N번째까지 누적합

for i in range(1, N + 1):
    prefix_sum[i] += prefix_sum[i - 1] + arr[i - 1]     # 누적합

# print(prefix_sum)

left = 0
right = 1
ans = 100000    # 구간 길이 최솟값. 최댓값으로 초기화

while left < N:     # 누적합 인덱스는 N번까지. left가 N번에 가면 종료
    if prefix_sum[right] - prefix_sum[left] >= S:   # 구간합이 S 이상
        tmp = right - left  # 구간의 길이
        if ans > tmp:   # 더 작은 값이면
            ans = tmp   # 답 갱신
        left += 1   # 구간 시작점 옮겨 더 짧은 구간으로 만들어서 되는지 확인

    else:       # 구간합이 S가 안 되면
        if right < N:   # 아직 구간이 누적합 끝까지 가보지 않았으면
            right += 1  # 구간의 끝 늘려서 구해봄
        else:
            left = N    # 구간이 끝까지 가봤는데도 S가 안 된 거면 그냥 바로 종료시켜도 되지 않나

if prefix_sum[-1] < S:  # 다 합해도 S가 되지 못할 경우
    ans = 0

print(ans)