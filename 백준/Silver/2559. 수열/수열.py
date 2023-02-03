# 백준 2559 수열

N, K = map(int, input().split())

temp = list(map(int, input().split()))

# 누적합 리스트
prefix_sum = [0] * N

prefix_sum[0] = temp[0]

for i in range(1, N):
    prefix_sum[i] = prefix_sum[i - 1] + temp[i]

# 연속 온도 합. 첫 구간은 넣고 시작
con_temp_sum = [prefix_sum[K - 1]]

# 구간의 종점을 i로 둠
for i in range(K, N):
    con_temp_sum.append(prefix_sum[i] - prefix_sum[i - K])

print(max(con_temp_sum))

