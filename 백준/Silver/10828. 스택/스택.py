# 10828. 스택
import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    command = input().strip()
    if command == "pop":
        print(stack.pop() if stack else -1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        print(0 if stack else 1)
    elif command == "top":
        print(stack[-1] if stack else -1)
    else:
        c, int_str = command.split()
        stack.append(int(int_str))
