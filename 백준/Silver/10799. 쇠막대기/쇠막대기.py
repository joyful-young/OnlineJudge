# 백준 10799. 쇠막대기

string = input()
L = len(string)

stack = [0] * L
top = -1        # 스택 초기화

ans = 0
i = 0
while i < L:
    if string[i] == '(':
        if string[i:i + 2] != '()':     # 레이저 아니면
            top += 1        # 스택에 push
            stack[top] = string[i]
            ans += 1        # 막대 개수 늘어남
            i += 1
        else:       # 레이저이면 막대 잘림
            ans += top + 1      # 스택에 남아있는 '(' 개수만큼 막대 개수 늘어남
            i += 2      # '()' 다음부터 확인해봐야
    else:       # ')'일 경우
        if top > -1:
            top -= 1        # '(' 하나 빼냄
            i += 1

print(ans)