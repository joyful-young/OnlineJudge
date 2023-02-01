import sys

N, M = map(int, sys.stdin.readline().split())

string_set = set()

for _ in range(N):
    string_set.add(sys.stdin.readline().rstrip())
cnt = 0
for _ in range(M):
    if sys.stdin.readline().rstrip() in string_set:
        cnt += 1
print(cnt)