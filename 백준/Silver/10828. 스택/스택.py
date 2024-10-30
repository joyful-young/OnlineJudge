# 10828. 스택
import sys
input = sys.stdin.readline

N = int(input())
stack = [-1 for _ in range(10000)]
top = -1

for _ in range(N):
    command = input().strip()
    if command == "pop":
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            top -= 1
    elif command == "size":
        print(top + 1)
    elif command == "empty":
        print(1 if top == -1 else 0)
    elif command == "top":
        print(stack[top] if top != -1 else -1)
    else:
        c, int_str = command.split()
        top += 1
        stack[top] = int(int_str)

