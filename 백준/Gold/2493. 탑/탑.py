# 백준 2493 탑

N = int(input())

tower = list(map(int, input().split()))

# 받은 탑 순서 거꾸로
tower.reverse()

stack = [0]

ans_reversed = [0] * N

for i in range(1, N):
    while stack and tower[stack[-1]] < tower[i]:
        ans_reversed[stack.pop()] = N - i
    stack.append(i)

ans = reversed(ans_reversed)

print(*ans)
