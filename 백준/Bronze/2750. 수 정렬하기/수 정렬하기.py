import sys

# N 입력
N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))

numbers.sort()

for i in numbers:
    print(i)