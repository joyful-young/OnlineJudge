# 백준 11399. ATM

N = int(input())

arr = list(map(int, input().split()))   # 인출 소요 시간

# 빨리 인출하는 사람부터
arr.sort()  # 오름차순 정렬

# 누적합 구하기
for i in range(1, N):
    arr[i] += arr[i - 1]

# 각 사람이 돈을 인출하는 데 필요한 시간의 합
print(sum(arr))
