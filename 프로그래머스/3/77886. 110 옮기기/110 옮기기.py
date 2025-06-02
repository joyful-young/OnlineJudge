def solution(s):
    return [change(x) for x in s]


def change(string):
    stack = []
    cnt = 0
    for c in string:
        if c == "0" and len(stack) >= 2 and stack[-1] == "1" and stack[-2] == "1":
            stack.pop()
            stack.pop()
            cnt += 1
        else:
            stack.append(c)
    
    ones = 0
    last_zero = -1
    for i in range(len(stack)):
        if stack[i] == "1":
            ones += 1
            if ones >= 2:
                break
        else:
            last_zero = i
            ones = 0
            
    if last_zero == -1:
        return "".join(["110"] * cnt + stack)
    else:
        return "".join(stack[:last_zero + 1] + ["110"] * cnt + stack[last_zero + 1:])
    