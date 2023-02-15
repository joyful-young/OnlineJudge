# 백준 11055. 가장 큰 증가 부분 수열

N = int(input())
A = list(map(int, input().split()))

S = [0] * N    # 그 위치 원소를 마지막으로 하는 A의 증가 부분 수열의 합
S[0] = A[0]

for i in range(1, N):       # A의 두번째 원소부터 끝까지
    tmp_max = 0
    for j in range(i, -1, -1):      # i번 원소부터 거꾸로 가면서 비교
        if A[i] > A[j]:         # 증가수열이면
            if S[j] > tmp_max:      # 이전까지의 증가수열 합 중 가장 큰 값
                tmp_max = S[j]
    S[i] = tmp_max + A[i]           # 그 값에 원소 더하기

print(max(S))