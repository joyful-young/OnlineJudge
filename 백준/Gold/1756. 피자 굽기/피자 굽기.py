# 백준 1756. 피자 굽기
import sys
input = sys.stdin.readline
D, N = map(int, input().split())
arr = list(map(int, input().split()))   # 0 ~ (D - 1)

pizza = list(map(int, input().split()))     # 0 ~ (N - 1)

for i in range(D - 1):
    if arr[i + 1] > arr[i]:     # 아래 깊이 지름이 더 커도 위의 더 작은 지름만큼만 들어갈 수 있음
        arr[i + 1] = arr[i]     # 아래로 내려가면서 갱신

idx = 0     # 넣어야 할 피자번호
for i in range(D - 1, -1, -1):      # 오븐 제일 깊은 곳부터
    if pizza[idx] <= arr[i]:    # 들어갈 수 있으면
        idx += 1    # 다음 피자

    if idx == N:    # 다 넣었으면
        print(i + 1)    # 마지막 피자 반죽 위치
        break

else:       # 다 못 넣었으면
    print(0)
