import sys
input = sys.stdin.readline


r1, c1, r2, c2 = map(int, input().split())

# 출력할 배열 크기
R = r2 - r1 + 1
C = c2 - c1 + 1

# 배열 초기화
arr = [[-1] * C for _ in range(R)]

# arr[r][c]에 들어갈 숫자 계산
def calc_number(r, c):
    # 소용돌이 크기
    k = max(abs(r), abs(c))
    # 오른쪽 아래 꼭짓점 숫자
    right_down = (2 * k + 1) ** 2
    
    if r == k:
        # 아랫변
        return right_down - (k - c)
    elif c == -k:
        # 왼쪽 변
        return right_down - 2 * k - (k - r)
    elif r == -k:
        # 윗변
        return right_down - 4 * k - (k + c)
    else:
        # 오른쪽 변
        return right_down - 6 * k - (k + r)

max_n = 0
for r in range(r1, r2 + 1):
    for c in range(c1, c2 + 1):
        v = calc_number(r, c)
        arr[r - r1][c - c1] = v
        if v > max_n:
            max_n = v

# 가장 긴 숫자 길이
max_l = len(str(max_n))

results = []
for row in arr:
    # f"{v:>{max_l}}" v 값을 폭 max_l 공간에서 오른쪽 정렬(>)
    results.append(" ".join(f"{v:>{max_l}}" for v in row))
print("\n".join(results))
