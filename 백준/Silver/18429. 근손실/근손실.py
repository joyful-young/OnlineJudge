# 백준 SWEA 18429. 근손실
def f(i, k, w):
    global cnt
    if i == k:
        cnt += 1
    else:
        for j in range(k):
            if not used[j] and w + A[j] >= 500:     # 쓰지 않은 키트고 중량이 500이상이 되는 경우에만
                used[j] = 1
                f(i + 1, k, w + A[j])
                used[j] = 0


N, K = map(int, input().split())    # N 운동 키트 개수, K 하루 근손실
A = list(map(int, input().split()))

weight = 500
A = [A[i] - K for i in range(N)]    # 운동 키트 사용 시 하루 중량 변화
used = [0] * N
cnt = 0
f(0, N, weight)

print(cnt)