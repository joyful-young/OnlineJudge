N = int(input())

for _ in range(N):
    stack = []
    input_str = input()
    for l in input_str:
        # '('는 스택에 바로 넣음
        if l == '(':
            stack.append(l)
        # ')'는
        else:
            # 스택이 비지 않았으면('('가 들어있으면)
            if stack:
                # 들어있던 '(' 제거
                stack.pop()
            # 스택이 비었으면 NO 출력 후 break
            else:
                print('NO')
                break
    # for문이 다 돌았을 때
    else:
        # 스택이 비어있지 않으면(짝없는 '('가 있으면) NO
        if stack:
            print('NO')
        # 스택이 비어있으면 YES
        else:
            print('YES')