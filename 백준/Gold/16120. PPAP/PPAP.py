s = input()
stack = []
for c in s:
    stack.append(c)
    if len(stack) >= 4 and stack[-4:] == ["P", "P", "A", "P"]:
        for _ in range(3):
            stack.pop()
if stack == ["P"]:
    print("PPAP")
else:
    print("NP")