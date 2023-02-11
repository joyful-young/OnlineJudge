import sys


N, M = map(int, sys.stdin.readline().split())

not_heard = set()
not_seen = set()
for _ in range(N):
    not_heard.add(sys.stdin.readline().rstrip())
    
for _ in range(M):
    not_seen.add(sys.stdin.readline().rstrip())

inter = list(not_heard & not_seen)
print(len(inter))
inter.sort()

for i in inter:
    print(i)