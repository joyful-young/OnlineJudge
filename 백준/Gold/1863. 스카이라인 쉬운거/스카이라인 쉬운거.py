# 백준 1863. 스카이라인 쉬운거
import sys
input = sys.stdin.readline

n = int(input())
stack = []
cnt = 0
arr = [list(map(int, input().split())) for _ in range(n)] + [[1000000, 0]]

for i in range(n + 1):
    h = arr[i][1]
    if not stack:
        stack.append(h)
    else:
        if stack[-1] < h:
            stack.append(h)
        else:
            while stack and stack[-1] > h:
                stack.pop()
                cnt += 1
            if stack and stack[-1] == h:
                stack.pop()
            stack.append(h)

print(cnt)
