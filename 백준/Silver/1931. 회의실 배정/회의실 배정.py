# 백준 1931. 회의실 배정

N = int(input())

arr = [0] * N

for i in range(N):
    arr[i] = list(map(int, input().split()))

# print(arr)

arr.sort(key=lambda x: x[0])    # 하위 우선순위
arr.sort(key=lambda x: x[1])    # 상위 우선순위

# print(arr)

# # 틀려서 새로 추가한 부분
# # 첫 회의 찾기 - 가장 빠른 시간에 끝나는 것
# tmp = arr[0][1]     # 가장 빠른 종료 시간
# min_idx = 0
# for i in range(N):
#     if arr[i][1] != tmp:    # 종료시간 다르면 break
#         break
#     if arr[i][0] < arr[min_idx][0]:     # 종료시간 같고 시작시간 더 빠른 게 있으면 그것부터
#         min_idx = i

# 첫 회의
m = arr[0]
cnt = 1

i = 1       # i 초기화
while i < N:
    if arr[i][0] >= m[1]:       # 회의 시작 시간이 이전 회의 종료시간 이상이면
        cnt += 1
        m = arr[i]              # 그게 다음 회의
    i += 1

print(cnt)