import sys
input = sys.stdin.readline

# 소용돌이 방향. 우-상-좌-하
# 상->좌일 때 거리 1 증가해야 함
DIR = [(0, 1), (-1, 0), (0, -1), (1, 0)]

r1, c1, r2, c2 = map(int, input().split())
# 소용돌이 크기
S = max(abs(r1), abs(c1), abs(r2), abs(c2))

# 출력할 배열 크기
R = r2 - r1 + 1
C = c2 - c1 + 1

# 출력할 배열
arr = [[-1] * C for _ in range(R)]


def is_valid(nr, nc):
    return 0 <= nr < R and 0 <= nc < C


# 배열 채우기
# 원점
r, c = -r1, -c1
num = 1
if is_valid(r, c):
    arr[r][c] = num
num += 1

size = -1
d = 0
l = 1

max_v = 0
while size < S:
    # 직진
    for _ in range(l):
        r += DIR[d][0]
        c += DIR[d][1]
        
        if is_valid(r, c):
            arr[r][c] = num
            max_v = num
        num += 1
    
    # 방향 바꾸기
    if d == 0:
        size += 1
    elif d == 1 or d == 3:
        l += 1
    
    d = (d + 1) % 4
    
#TODO
max_l = len(str(max_v))
results = []
for row in arr:
    # f"{v:>{max_l}}" v 값을 폭 max_l 공간에서 오른쪽 정렬(>)
    results.append(" ".join(f"{v:>{max_l}}" for v in row))
print("\n".join(results))
