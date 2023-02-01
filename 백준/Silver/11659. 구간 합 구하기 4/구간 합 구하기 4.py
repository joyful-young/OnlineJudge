import sys

# N, M입력
N, M = map(int, sys.stdin.readline().split())

# 숫자 리스트 입력
n_list = list(map(int, sys.stdin.readline().split()))

# 편의를 위해 0을 넣어놓고 시작
sum_list = [0]
for i in range(0, N):
    sum_list.append(sum_list[i] + n_list[i])

# j번째 숫자까지 합은 sum_list에서 인덱스가 j
# i번째 수부터 j번째 수까지 합은 sum_list[j] - sum_list[i - 1]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sum_list[j] - sum_list[i - 1])