# 백준 11053. 가장 긴 증가하는 부분 수열

N = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(N)]  # i번째 원소까지 가장 긴 증가하는 부분 수열 길이

for i in range(N):          # i번 인덱스 원소
    for j in range(i):      # (i - 1)번 원소까지와 비교
        if arr[i] > arr[j]:     # i번째 원소가 더 크면
            dp[i] = max(dp[i], dp[j] + 1)       # 이전까지 계산된 dp[i] 값과 j번째 원소에서 연장된 수열 길이 중 더 큰 값

print(max(dp))
