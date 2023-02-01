# 백준 10828
import sys

N = int(sys.stdin.readline())

# 빈 스택
stack = []

for _ in range(N):
    command = sys.stdin.readline().rstrip()

    # push 명령어 골라내기
    if command[-1].isdigit():
        stack.append(int(command.split()[-1]))

    # push 명령어가 아닐 경우
    else:
        if command == 'pop':
            # 가장 위 정수 빼고 그 수 출력
            if stack:
                num = stack.pop()
                print(num)
            # 스택이 비었으면 -1 출력
            else:
                print(-1)

        # 스택 내 정수 개수 출력
        elif command == 'size':
            print(len(stack))

        elif command == 'empty':
            # 스택 비지 않았으면 0
            if stack:
                print(0)
            # 스택이 비었으면 1
            else:
                print(1)

        elif command == 'top':
            # 스택 가장 위 정수 출력
            if stack:
                print(stack[-1])
            # 스택 비었으면 -1
            else:
                print(-1)