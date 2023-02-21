# 1931 백준 회의실 , 그리디
N = int(input())
li = []
for tc in range(N):
    x, y = list(map(int,input().split()))
    li.append([x,y])

sor = sorted(li, key=lambda x: (x[1],x[0])) # 시작시간 오름차순때리고 끝나는시간 오름차순때림


start = sor[0][0]
end = sor[-1][-1]

time = [[sor[0][0],sor[0][1]]] # 최대가능한 회의시간

end_time = sor[0][1] #끝시간 세팅했음 ~
for i in range(1, len(sor)): # 젤 처음꺼 넣어놨따
    if end_time <= sor[i][0]:
        time.append([sor[i][0],sor[i][1]])
        end_time = sor[i][1]
print(len(time))
