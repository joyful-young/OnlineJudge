# 백준 1874. 스택수열

import sys

n = int(sys.stdin.readline())

input_data = [0] * n    # 입력 숫자
for i in range(n):
    input_data[i] = int(sys.stdin.readline())

ans = list()   # 답

n_to_one = list(range(n, 0, -1))    # 내림차순

stack = list()

for i in range(n):
    if stack and stack[-1] > input_data[i]:     # 스택 마지막 수가 나와야 할 수열 수보다 크면
        print('NO')     # 수열 생성 불가
        break           # for문 break
    while not stack or stack[-1] < input_data[i]:   # 스택이 비었거나 나올 수보다 스택 마지막 수가 작으면
        stack.append(n_to_one.pop())        # 아직 안 넣은 수 스택에 넣기
        ans.append('+')
    if stack and stack[-1] == input_data[i]:        # 스택 마지막 수가 수열 수와 같으면
        stack.pop()     # 내보냄
        ans.append('-')
else:
    for i in range(n * 2):
        print(ans[i])