N = int(input())

lst =[]

for _ in range(N):
    lst.append(list(map(int, input().split())))

rank = []    
for i in range(N):
    cnt = 0
    for j in range(N):
        if i == j:
            continue
        else:
            if lst[j][0] > lst[i][0] and lst[j][1] > lst[i][1]:
                cnt += 1
    rank.append(cnt + 1)

print(*rank)