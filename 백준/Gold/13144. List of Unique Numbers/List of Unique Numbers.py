# 13144. List of Unique Numbers

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

cnt = 0
left = 0

num_set = set()
for right in range(N):
    while numbers[right] in num_set:
        num_set.remove(numbers[left])
        left += 1
    num_set.add(numbers[right])
    cnt += right - left + 1

print(cnt)
