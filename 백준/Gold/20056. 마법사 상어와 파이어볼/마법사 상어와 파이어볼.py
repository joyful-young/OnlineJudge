import sys
input = sys.stdin.readline

dr = [-1, -1, 0, 1, 1, 1, 0, -1]    # 방향 번호 0 ~ 7
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def divide(fireball_list):
    n = len(fireball_list)
    sum_of_m, sum_of_s, first_d = fireball_list[0]
    dir_flag = True
    
    for m, s, d in fireball_list[1:]:
        sum_of_m += m
        sum_of_s += s
        if (d - first_d) % 2:
            dir_flag = False

    new_m = sum_of_m // 5
    # 질량 0인 파이어볼 소멸
    if new_m == 0:
        return []

    d_list = [0, 2, 4, 6] if dir_flag else [1, 3, 5, 7]
    return [(new_m, sum_of_s // n, d_list[i]) for i in range(4)]


def move(fireball_dict):
    # 1. 모든 파이어볼 d 방향으로 s칸 만큼 이동
    moved = {}
    for pos, fireball_list in fireball_dict.items():
        r, c = pos
        for m, s, d in fireball_list:
            nr = (r + s * dr[d]) % N
            nc = (c + s * dc[d]) % N
            if (nr, nc) in moved:
                moved[(nr, nc)].append((m, s, d))
            else:
                moved[(nr, nc)] = [(m, s, d)]

    # 2. 파이어볼 합치기 & 나누기
    for pos, fireball_list in moved.items():
        if len(fireball_list) > 1:
            moved[pos] = divide(fireball_list)

    # 파이어볼 없는 좌표는 제외하고 반환
    return {k: v for k, v in moved.items() if v}

N, M, K = map(int, input().split())

# (r, c): [(m, s, d), ...]
fireballs = {}
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    # 파이어볼 위치 같은 경우는 입력으로 주어지지 않음
    fireballs[(r - 1, c - 1)] = [(m, s, d)]

for _ in range(K):
    fireballs = move(fireballs)

# 남은 파이어볼 질량 합 구하기
total_m = 0
for fbs in fireballs.values():
    for fb in fbs:
        total_m += fb[0]

print(total_m)
