N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
current = 0
min_len = N + 1

while True:
    # S 이상이면 시작점 옮겨 더 짧은 구간도 가능한지 확인
    if current >= S:
        min_len = min(min_len, end - start)
        current -= arr[start]
        start += 1
    elif end == N:
        break
    else:    # S 미만이면 끝점 옮겨 더 긴 구간 확인
        current += arr[end]
        end += 1

print(min_len if min_len != N + 1 else 0)
