parenthesis = input()
N = len(parenthesis)

left = parenthesis.count("(")
right = N - left

answer = 0
if left < right:
    total = 0
    for c in parenthesis:
        if c == ")":
            total -= 1
            answer += 1
        else:
            total += 1
            
        if total < 0:
            break
elif left > right:
    total = 0
    for c in parenthesis[::-1]:
        if c == "(":
            total += 1
            answer += 1
        else:
            total -= 1

        if total > 0:
            break
print(answer)
