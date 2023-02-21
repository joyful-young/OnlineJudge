# 백준 1026. 보물

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# B는 재배열하지 말랬지만 A를 맘대로 재배열할 수 있는 이상 무의미
# 제일 큰 수에 제일 작은 수 곱하기
A.sort()    # 오름차순
B.sort(reverse=True)    # 내림차순

S = 0
for i in range(N):
    S += A[i] * B[i]

print(S)
