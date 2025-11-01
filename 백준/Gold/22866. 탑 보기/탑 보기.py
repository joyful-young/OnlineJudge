import sys
input = sys.stdin.readline


N = int(input())
heights = list(map(int, input().split()))


def look(rg):
    cnts = [0] * N
    nearest = [None] * N
    stack = []
    for i in rg:
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()
        cnts[i] = len(stack)

        if stack:
            nearest[i] = stack[-1]

        stack.append(i)
    return cnts, nearest


left_cnts, left_near = look(range(N))
right_cnts, right_near = look(range(N - 1, -1, -1))

for i in range(N):
    # i 양쪽으로 볼 수 있는 건물 총 개수
    total = left_cnts[i] + right_cnts[i]
    if total == 0:
        print(0)
        continue

    if right_near[i] is None:
        nearest = left_near[i]
    elif left_near[i] is None:
        nearest = right_near[i]
    else:
        l_dist = i - left_near[i]
        r_dist = right_near[i] - i
        if l_dist <= r_dist:
            nearest = left_near[i]
        else:
            nearest = right_near[i]
    print(total, nearest + 1)