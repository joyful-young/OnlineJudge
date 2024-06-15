# 1765. 닭싸움 팀 정하기

def find(student):
    while rep[student] != student:
        student = rep[student]
    return student


def union(x, y):
    rep[find(y)] = find(x)


n = int(input())
m = int(input())

rep = [i for i in range(n + 1)]
enemy = [[] for _ in range(n + 1)]

for _ in range(m):
    s, a, b = input().split()
    a = int(a)
    b = int(b)
    if s == "E":
        enemy[a].append(b)
        enemy[b].append(a)
    else:
        union(a, b)

for enemy_list in enemy[1:]:
    if len(enemy_list) >= 2:
        for i in range(len(enemy_list)):
            for k in range(i + 1, len(enemy_list)):
                union(enemy_list[i], enemy_list[k])

teams = set()
for i in range(1, n + 1):
    teams.add(find(i))

print(len(teams))
