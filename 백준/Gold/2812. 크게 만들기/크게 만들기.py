N, K = map(int, input().split())
number = list(map(int, input().strip()))

stk = []
cnt = 0
for n in number:
    while stk and stk[-1] < n and cnt < K:
        stk.pop()
        cnt += 1
    stk.append(n)

print("".join(map(str, stk[:N - K])))
