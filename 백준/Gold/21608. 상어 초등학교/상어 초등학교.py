import sys
input = sys.stdin.readline

DIR = [(-1, 0), (0, -1), (0, 1), (1, 0)]
N = int(input())
S = N * N
students = []
like = [set() for _ in range(S + 1)]

arr = [[[-1, 4] for _ in range(N)] for _ in range(N)]
for r in range(N):
    for c in range(N):
        if not (r == 0 or c == 0 or r == N - 1 or c == N - 1):
            continue
        
        if (r, c) in [(0, 0), (0, N - 1), (N - 1, 0), (N - 1, N - 1)]:
            arr[r][c][1] = 2
        else:
            arr[r][c][1] = 3

for _ in range(S):
    student, *like_set = list(map(int, input().split()))
    students.append(student)
    like[student] = set(like_set)


def arrange_seat(student, like_set):
    like_cnt = 0
    # (인접한 빈칸 개수, 행 번호, 열 번호)
    candidates = []
    for r in range(N):
        for c in range(N):
            if arr[r][c][0] != -1:
                continue

            # 빈칸일 경우
            cnt = 0
            for dr, dc in DIR:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc][0] in like_set:
                    cnt += 1
            if cnt > like_cnt:
                like_cnt = cnt
                candidates = [(arr[r][c][1], r, c)]
            elif cnt == like_cnt:
                candidates.append((arr[r][c][1], r, c))

    candidates.sort(key=lambda x:(-x[0], x[1], x[2]))

    # 자리배치
    r, c = candidates[0][1:]
    arr[r][c][0] = student
    for dr, dc in DIR:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            arr[nr][nc][1] -= 1


def get_satisfaction():
    ans = 0
    for r in range(N):
        for c in range(N):
            like_set = like[arr[r][c][0]]
            cnt = 0
            for dr, dc in DIR:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc][0] in like_set:
                    cnt += 1

            if cnt == 0:
                continue
            ans += 10 ** (cnt - 1)
    return ans
            

for student in students:
    arrange_seat(student, like[student])

print(get_satisfaction())