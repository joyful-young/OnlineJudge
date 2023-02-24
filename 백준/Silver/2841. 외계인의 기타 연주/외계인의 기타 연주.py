N, P = map(int,input().split())
li = [[] for _ in range(8)]
# N이 뭐가있는지 받아놓자..
cnt = 0
for i in range(N):
    st, num = map(int,input().split())
    if not li:
        li[st].append(num)
        cnt += 1
    else:
        while li[st] and num < li[st][-1]:
            li[st].pop()
            cnt += 1
        if not li[st] or num > li[st][-1]:
            li[st].append(num)
            cnt += 1
        else:
            pass
print(cnt)
