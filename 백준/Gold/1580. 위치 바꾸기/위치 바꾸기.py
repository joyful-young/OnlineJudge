import sys
from collections import deque
input = sys.stdin.readline

DIR = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (0, 0)]


N, M = map(int, input().split())
arr = [""] * N
Ar = Ac = Br = Bc = None
for r in range(N):
    arr[r] = input().rstrip()
    for c in range(M):
        if arr[r][c] == "A":
            Ar, Ac = r, c
        elif arr[r][c] == "B":
            Br, Bc = r, c

start = (Ar, Ac, Br, Bc)
goal = (Br, Bc, Ar, Ac)

def is_valid(r, c):
    return 0 <= r < N and 0 <= c < M and arr[r][c] != "X"

    
q = deque([(Ar, Ac, Br, Bc, 0)])
visited = {start}

while q:
    ar, ac, br, bc, t = q.popleft()

    if (ar, ac, br, bc) == goal:
        print(t)
        break

    for adr, adc in DIR:
        anr, anc = ar + adr, ac + adc
        if not is_valid(anr, anc):
            continue

        for bdr, bdc in DIR:
            bnr, bnc = br + bdr, bc + bdc
            if not is_valid(bnr, bnc):
                continue

            if anr == bnr and anc == bnc:
                # 같은 칸으로 가면 안 됨
                continue

            if anr == br and anc == bc and bnr == ar and bnc == ac:
                # 교차는 안 됨
                continue

            state = (anr, anc, bnr, bnc)
            if state not in visited:
                visited.add(state)
                q.append((anr, anc, bnr, bnc, t + 1))
else:
    print(-1)