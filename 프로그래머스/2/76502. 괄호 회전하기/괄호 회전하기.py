def solution(s):
    N = len(s)
    new_s = s + s[:N - 1]
    answer = 0
    for i in range(N):
        if check(new_s[i:i + N]):
            answer += 1
    return answer


def check(target):
    stack = []
    for t in target:
        if t in ["(", "[", "{"]:
            stack.append(t)
        else:
            if not stack:
                return False
            if (t == ")" and stack[-1] == "(") or (t == "]" and stack[-1] == "[") or (t == "}" and stack[-1] == "{"):
                stack.pop()
            else:
                return False
    return True if not stack else False