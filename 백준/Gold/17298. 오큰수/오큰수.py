N = int(input())

num_lst = list(map(int, input().split()))

stack = []

# 조건에 안 맞으면 -1 나오게
result = [-1] * N

stack.append(0)

for idx in range(1, N):
    while stack and (num_lst[idx] > num_lst[stack[-1]]):
        result[stack.pop()] = num_lst[idx]
    stack.append(idx)

print(*result)