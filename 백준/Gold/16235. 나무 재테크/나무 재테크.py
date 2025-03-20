import sys
input = sys.stdin.readline
from collections import defaultdict

# 인접칸
adj = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

N, M, K = map(int, input().split())
A = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

# 현재 양분
arr = [[5 for _ in range(N + 1)] for _ in range(N + 1)]

# key: (r, c), value: [나무들의 나이. 오름차순 유지]
trees = defaultdict(list)
for _ in range(M):
    r, c, age = map(int, input().split())
    trees[(r, c)].append(age)

for _ in range(K):
    # 봄 여름
    reproduct = defaultdict(int)    # 가을에 (r, c)에서 번식할 나무 수
    for (r, c) in trees.keys():
        for idx in range(len(trees[(r, c)])):
            age = trees[(r, c)][idx]
            if arr[r][c] >= age:
                arr[r][c] -= age
                trees[(r, c)][idx] += 1
                if (age + 1) % 5 == 0:
                    reproduct[(r, c)] += 1
            else:
                arr[r][c] += sum([age // 2 for age in trees[(r, c)][idx:]])
                trees[(r, c)] = trees[(r, c)][:idx]
                break

    # 가을
    for (r, c), num in reproduct.items():
        for dr, dc in adj:
            nr, nc = r + dr, c + dc
            if 1 <= nr <= N and 1 <= nc <= N:
                trees[(nr, nc)] = [1] * num + trees[(nr, nc)]

    # 겨울
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            arr[r][c] += A[r][c]

print(sum(len(ages) for ages in trees.values()))
