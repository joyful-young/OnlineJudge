N = int(input())
developers = list(map(int, input().split()))

left = 0
right = N - 1
max_v = 0

while left < right:
    max_v = max(max_v, (right - left - 1) * min(developers[left], developers[right]))

    if developers[left] < developers[right]:
        left += 1
    else:
        right -= 1

print(max_v)