import sys
input = sys.stdin.readline

di = [-1, 0, 1, 0]    # 북, 동, 남, 서
dj = [0, 1, 0, -1]

N, M = map(int, input().split())
R, C, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 청소 여부
visited = [[0 for _ in range(M)] for _ in range(N)]

def get_next_room(r, c, d):
    for _ in range(4):
        d = (d - 1) % 4
        nr, nc = r + di[d], c + dj[d]
        if arr[nr][nc] == 0 and visited[nr][nc] == 0:
            return (nr, nc, d)
    return None


def clean(si, sj, d):
    visited[si][sj] = 1

    next_room = get_next_room(si, sj, d)
    if next_room is not None:
        return clean(*next_room)

    # 후진 필요
    ni, nj = si - di[d], sj - dj[d]
    if arr[ni][nj] == 0:
        return clean(ni, nj, d)

    return

clean(R, C, D)
print(sum([sum(visited[i]) for i in range(N)]))
