# 백준 2631. 줄세우기
import sys
input = sys.stdin.readline
N = int(input())

dp = [1] * N        # 최장증가수열 구하기
arr = [0] * N       # 초기 아이들 순서

arr[0] = int(input())

for i in range(N - 1):
    arr[i + 1] = int(input())
    for j in range(i + 1):      # 0부터 i번 인덱스까지
        if arr[j] < arr[i + 1]:
            dp[i + 1] = max(dp[i + 1], dp[j] + 1)

# print(dp)
print(N - max(dp))      # 전체 인원 수에서 최장증가수열의 길이를 뺀 게 옮겨지는 아이들의 최소 수