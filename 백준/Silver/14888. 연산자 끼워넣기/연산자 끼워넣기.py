import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
plus, sub, mul, div = map(int, input().split())
operators = [0] * plus + [1] * sub + [2] * mul + [3] * div
visited = [0 for _ in range(N - 1)]
perm = [-1 for _ in range(N - 1)]

max_value = -1000000000
min_value = 1000000000

def calc(oper_perm, number):
    for i in range(N - 1):
        if oper_perm[i] == 0:
            number += A[i + 1]
        elif oper_perm[i] == 1:
            number -= A[i + 1]
        elif oper_perm[i] == 2:
            number *= A[i + 1]
        else:
            if number < 0:
                number = -((-number) // A[i + 1])
            else:
                number //= A[i + 1]
    return number


def get_perm(x, k):
    """
    perm[x] 값 정하기
    """
    global max_value
    global min_value
    
    if x == k:
        temp = calc(perm, A[0])
        max_value = max(max_value, temp)
        min_value = min(min_value, temp)
        return

    for i in range(N - 1):
        if visited[i] == 1:
            continue

        visited[i] = 1
        perm[x] = operators[i]
        get_perm(x + 1, k)
        visited[i] = 0

get_perm(0, N - 1)
print(max_value)
print(min_value)