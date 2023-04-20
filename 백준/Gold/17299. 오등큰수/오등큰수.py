# 백준 17299. 오등큰수

N = int(input())
arr = list(map(int, input().split()))   # 주어진 숫자

# 등장횟수 배열
count = [0] * (max(arr) + 1)
for i in range(N):
    count[arr[i]] += 1

# print(count)
ans = [-1] * N

stack = [0]     # 첫 번째 인덱스

for i in range(1, N):
    while stack and count[arr[i]] > count[arr[stack[-1]]]:
        ans[stack.pop()] = arr[i]
    stack.append(i)

print(*ans)