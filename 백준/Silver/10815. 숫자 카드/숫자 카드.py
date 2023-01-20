N = int(input())
have = set(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

for i in numbers:
    if i in have:
        print(1, end=' ')
    else:
        print(0, end=' ')
