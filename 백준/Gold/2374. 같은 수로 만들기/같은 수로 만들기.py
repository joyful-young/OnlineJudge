# 2374. 같은 수로 만들기
import sys
input = sys.stdin.readline


N = int(input())
numbers = [int(input()) for _ in range(N)]
stack = []
cnt = 0
idx = 0
while idx < N:
    number = numbers[idx]
    if stack and stack[-1] < number:
        if len(stack) >= 2 and stack[-2] < number:
            cnt += stack[-2] - stack[-1]
            stack.pop()
            continue
        else:
            cnt += number - stack[-1]
            stack[-1] = number
    elif not stack or stack[-1] > number:
        stack.append(number)
    
    idx += 1

if len(stack) >= 2:
    cnt += stack[0] - stack[-1]

print(cnt)