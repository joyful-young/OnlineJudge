# 백준 5397. 키로거
# 스택으로 풀기 ver.2

T = int(input())
for _ in range(T):
    cmd = input()

    # 커서 왼쪽
    left = []
    # 커서 오른쪽
    right = []

    for char in cmd:
        if char == '<' and left:    # 커서 왼쪽으로. 맨 앞 아님
            right.append(left.pop())
        elif char == '>' and right:     # 커서 오른쪽으로. 맨 뒤 아님
            left.append(right.pop())
        elif char == '-' and left:      # 백스페이스. 맨 앞 아님
            left.pop()
        elif (char != '<') and (char != '>') and (char != '-'):   # 보통 문자
            left.append(char)

    # 왼쪽은 그대로, 오른쪽은 거꾸로
    print(f"{''.join(left)}{''.join(right[::-1])}")
