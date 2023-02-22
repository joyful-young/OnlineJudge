# 백준 17413. 단어 뒤집기 2

string = input()
N = len(string)

stack = [0] * N
top = -1

ans = ''

i = 0
while i < N:
    if string[i] == '<':    # 태그 괄호가 나오면
        while top > -1:     # 스택 비우기
            top -= 1
            ans += stack[top + 1]

        while string[i] != '>':     # 닫는 괄호 나올 때까지
            ans += string[i]        # 문자 답에 넣기
            i += 1
        ans += '>'      # 마지막으로 닫는 괄호
    elif string[i] == ' ':       # 공백이면
        while top > -1:     # 스택이 빌 때까지
            top -= 1
            ans += stack[top + 1]   # pop 해서 답에 넣기
        ans += ' '
    else:       # 태그가 아닌 일반 문자이면
        top += 1
        stack[top] = string[i]      # 스택에 넣어놓기
    i += 1

while top > -1:     # 마지막으로 스택 비우기
    top -= 1
    ans += stack[top + 1]

print(ans)