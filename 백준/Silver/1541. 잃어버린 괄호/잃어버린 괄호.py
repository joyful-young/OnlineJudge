T = input().split('-')
T2 = [] # + 가 있으면 넣어줄거임
for i in T:
    if '+' in i: # 한개의 항목에 +가 있으면 !!!
        i2 = list(map(int,i.split('+'))) # + 기호로 나눠주고
        T2.append(sum(i2))
    else: # 없으면 바로넣어 !
        T2.append(int(i)) # << int로 해주는거는 0009 이런거때매;;
answer = T2[0] # 첫값이고
for i in T2[1:]:
    answer -= i
print(answer)
