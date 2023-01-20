num = []

import sys

for _ in range(5):
    num.append(int(sys.stdin.readline()))

num.sort()

print(int(sum(num) / 5))
print(num[2])