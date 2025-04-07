import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
plus, sub, mul, div = map(int, input().split())
operators = {
    0: plus,
    1: sub,
    2: mul,
    3: div
}

max_value = -1000000000
min_value = 1000000000
    

def calc(x, k, current):
    global max_value
    global min_value

    if x == k:
        max_value = max(max_value, current)
        min_value = min(min_value, current)
        return

    for oper, cnt in operators.items():
        if cnt == 0:
            continue

        operators[oper] -= 1
        if oper == 0:
            calc(x + 1, k, current + A[x + 1])
        elif oper == 1:
            calc(x + 1, k, current - A[x + 1])
        elif oper == 2:
            calc(x + 1, k, current * A[x + 1])
        else:
            if current < 0:
                calc(x + 1, k, -((-current) // A[x + 1]))
            else:
                calc(x + 1, k, current // A[x + 1])
        operators[oper] += 1

calc(0, N - 1, A[0])
print(max_value)
print(min_value)