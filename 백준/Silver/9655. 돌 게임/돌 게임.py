# 백준 9655. 돌 게임
# DP[N] = DP[N - 2]
# (N - 2)일 때 SK가 이기면 2개가 더 늘어나면 1개, 1개 -> SK가 이김
# DP[1] = SK, DP[2] = CY

N = int(input())
if N % 2:
    print('SK')
else:
    print('CY')