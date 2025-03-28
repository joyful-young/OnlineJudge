N = int(input())
statues = list(map(int, input().split()))

max_left = 0     # 왼쪽이 더 많을 때
max_right = 0    # 오른쪽이 더 많을 때
cur_left = 0
cur_right = 0

for i in range(N):
    if statues[i] == 1:
        cur_left += 1
        cur_right -= 1
    else:
        cur_left -= 1
        cur_right += 1

    max_left = max(max_left, cur_left)
    max_right = max(max_right, cur_right)

    if cur_left < 0:
        cur_left = 0
    if cur_right < 0:
        cur_right = 0

print(max(max_left, max_right))


