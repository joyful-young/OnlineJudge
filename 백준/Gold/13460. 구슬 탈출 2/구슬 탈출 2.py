import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0 for _ in range(N)]
for i in range(N):
    arr[i] = input().rstrip()
    for j in range(M):
        if arr[i][j] == "R":
            red_r, red_c = i, j
        elif arr[i][j] == "B":
            blue_r, blue_c = i, j

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]    # 상하좌우


def move(dir_key, rr, rc, br, bc):
    dr, dc = direction[dir_key]
    old_rr, old_rc, old_br, old_bc = rr, rc, br, bc

    while arr[br + dr][bc + dc] != "#" and arr[br][bc] != "O":
        br += dr
        bc += dc

    # B가 구멍에 R과 같이 또는 R보다 먼저 빠지면 안 됨
    if arr[br][bc] == "O":
        return False, rr, rc, br, bc

    while arr[rr + dr][rc + dc] != "#" and arr[rr][rc] != "O":
        rr += dr
        rc += dc

    # 공이 겹쳤을 경우
    if rr == br and rc == bc:
        if dir_key == 0:
            if old_rr < old_br:
                br += 1
            else:
                rr += 1
        elif dir_key == 1:
            if old_rr < old_br:
                rr -= 1
            else:
                br -= 1
        elif dir_key == 2:
            if old_rc < old_bc:
                bc += 1
            else:
                rc += 1
        else:
            if old_rc < old_bc:
                rc -= 1
            else:
                bc -= 1

    return True, rr, rc, br, bc


def bfs():
    q = deque([(red_r, red_c, blue_r, blue_c, 0)])
    visited = set()
    visited.add((red_r, red_c, blue_r, blue_c))

    while q:
        rr, rc, br, bc, cnt = q.popleft()

        if cnt >= 10:
            return -1
        
        for d in range(4):
            flag, new_rr, new_rc, new_br, new_bc = move(d, rr, rc, br, bc)
            
            if not flag:
                continue

            if arr[new_rr][new_rc] == "O":
                return cnt + 1

            if (new_rr, new_rc, new_br, new_bc) not in visited:
                visited.add((new_rr, new_rc, new_br, new_bc))
                q.append((new_rr, new_rc, new_br, new_bc, cnt + 1))

    return -1

print(bfs())
            
