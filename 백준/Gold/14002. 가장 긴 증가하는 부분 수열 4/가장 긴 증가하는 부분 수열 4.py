# 백준 14002. 가장 긴 증가하는 부분 수열 4

N = int(input())
A = list(map(int, input().split()))

D = [1] * N

for i in range(1, N):       # 확인할 A의 원소
    for j in range(i):
        if A[i] > A[j]:     # 증가수열이면
            D[i] = max(D[i], D[j] + 1)

L = max(D)      # 최장증가수열 길이

print(L)

ans = [0] * L   # 최장증가수열 초기화

max_idx = D.index(L)    # 최장 증가 수열의 끝의 인덱스

while max_idx >= 0:     # 인덱스가 0이 될 때까지
    if D[max_idx] == L:     # D 값이 수열 길이와 같으면
        ans[L - 1] = A[max_idx]     # 그 인덱스의 A 원소 넣기
        L -= 1
    max_idx -= 1

print(*ans)
