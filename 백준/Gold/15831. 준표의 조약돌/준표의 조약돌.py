import sys
input = sys.stdin.readline

N, B, W = map(int, input().split())
stones = input().rstrip()

left = -1
right = 0
black = 0
white = 0
max_v = 0
while right < N:
    # B 조건 만족 상태 유지
    # 새로운 조약돌 right
    if stones[right] == "W":
        white += 1
    else:
        black += 1

    if black <= B and white >= W:
        max_v = max(max_v, right - left)
    elif black > B:
        while left < right and black > B:
            left += 1
            if stones[left] == "W":
                white -= 1
            else:
                black -= 1

        if black <= B and white >= W:
            max_v = max(max_v, right - left)
    right += 1

print(max_v)
