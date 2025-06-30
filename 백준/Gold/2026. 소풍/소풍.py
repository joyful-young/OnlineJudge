import sys
input = sys.stdin.readline


K, N, F = map(int, input().split())
adjL = [set() for _ in range(N + 1)]
for _ in range(F):
    a, b = map(int, input().split())
    adjL[a].add(b)
    adjL[b].add(a)

candidates = [num for num in range(1, N + 1) if len(adjL[num]) >= K - 1]
used = [False] * len(candidates)
answer = []

def choose(s, n, lst):
    # n = len(candidates)
    if len(lst) == K:
        # K명 뽑음
        print("\n".join(map(str, lst)))
        sys.exit(0)  # 정답 찾았으므로 종료

    for i in range(s, n):
        # candidates[i]번 학생을 새로 선택
        # 이전에 뽑은 학생들(lst)과 다 연결되어 있어야
        if set(lst).issubset(adjL[candidates[i]]):
            lst.append(candidates[i])
            choose(i + 1, n, lst)
            lst.pop()

if K > len(candidates):
    print(-1)
else:
    choose(0, len(candidates), [])
    print(-1)

