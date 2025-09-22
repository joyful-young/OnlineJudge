import sys
from collections import defaultdict
input = sys.stdin.readline


DIR = {
    1: (0, 1),
    2: (0, -1),
    3: (-1, 0),
    4: (1, 0)
}

R_DIR = {
    1: 2,
	2: 1,
	3: 4,
	4: 3
}

N, K = map(int, input().split())
board = [[-1] * (N + 1)] + [[-1] + list(map(int, input().split())) for _ in range(N)]

# 위치별 말 번호 리스트
coord_map = defaultdict(list)

# 말 번호별 위치, 방향 정보
pieces = {}

for i in range(1, K + 1):
    r, c, d = map(int, input().split())
    pos = (r, c)
    pieces[i] = [pos, d]
    coord_map[pos].append(i)


def move(num):
    # num 번 말 옮기기
    # 말의 현재 위치, 방향
    pos, d = pieces[num]

    # 해당 위치 말들
    p = coord_map[pos]
    
    idx = p.index(num)
    upper = coord_map[pos][idx:]
    lower = coord_map[pos][:idx]

    # 이동할 위치
    nr = pos[0] + DIR[d][0]
    nc = pos[1] + DIR[d][1]
    new_pos = (nr, nc)

    if not (1 <= nr <= N and 1 <= nc <= N) or board[nr][nc] == 2:
        # 방향 반대로
        rev_d = R_DIR[d]
        nr = pos[0] + DIR[rev_d][0]
        nc = pos[1] + DIR[rev_d][1]
        
        if not (1 <= nr <= N and 1 <= nc <= N) or board[nr][nc] == 2:
            pieces[num][1] = rev_d
        else:
            new_pos = (nr, nc)

            if board[nr][nc] == 0:
                coord_map[new_pos] += upper
            else:
                coord_map[new_pos] += reversed(upper)

            if len(coord_map[new_pos]) >= 4:
                return True
                
            coord_map[pos] = lower
            pieces[num] = [new_pos, rev_d]
            for n in upper[1:]:
                pieces[n][0] = new_pos
    else:
        if board[nr][nc] == 0:
            coord_map[new_pos] += upper
        else:
            coord_map[new_pos] += reversed(upper)
        
        if len(coord_map[new_pos]) >= 4:
            return True
        
        coord_map[pos] = lower
        for n in upper:
            pieces[n][0] = new_pos
        return False

t = 1
while t <= 1000:
    flag = False
    for k in range(1, K + 1):
        flag = move(k)
        if flag:
            break

    if flag:
        print(t)
        break
    else:
        t += 1
else:
    print(-1)
