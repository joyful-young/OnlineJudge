# 백준 6198. 옥상 정원 꾸미기
import sys
input = sys.stdin.readline
N = int(input())
ans = [0] * N
stack = []
height = [0] * N
for i in range(N):
    h = int(input())
    height[i] = h
    if not stack:
        stack.append(i)
    elif height[stack[-1]] <= h:
        while stack and height[stack[-1]] <= h:
            idx = stack.pop()
            ans[idx] = i - idx - 1
        stack.append(i)
    else:
        stack.append(i)


# stack에 아직 남아있는 건물들은 높거나 같은 건물이 나오지 않은 건물
while stack:
    idx = stack.pop()
    ans[idx] = N - 1 - idx

print(sum(ans))
