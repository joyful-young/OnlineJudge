# 백준 9935. 문자열 폭발
# 스택에 쌓다가 같으면 없앰

string = input()
len_of_string = len(string)
bomb = input()
len_of_bomb = len(bomb)

stack = []

i = 0
while i < len_of_string:
    stack.append(string[i])
    if (len(stack) >= len_of_bomb) and stack[-len_of_bomb:] == list(bomb):
        for j in range(len_of_bomb):
            stack.pop()
    i += 1

if stack:
    print(''.join(stack))
else:
    print('FRULA')