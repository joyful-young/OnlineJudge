# 백준 11729 하노이 탑 이동 순서

# 맨 마지막 원판을 남기고 남은 그룹을 목표 장대가 아닌 곳에 옮긴 후
# 마지막 원판을 목표 장대로 옮기고
# 다시 남은 그룹을 목표 장대로 옮긴다

def move(num, start, end):
    if num > 1:
        move(num - 1, start, 6 - start - end)
        print(start, end)
        move(num - 1, 6 - start - end, end)

    else:
        print(start, end)


N = int(input())

# 이동횟수 f(n + 1) = f(n) + 1 + f(n)
# f(n) = 2^n - 1

print(2**N - 1)

move(N, 1, 3)