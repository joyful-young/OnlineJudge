# 백준 1436. 영화감독 숌

N = int(input())
num = 666
cnt = 1

while cnt < N:
    num += 1
    number = str(num)
    if '666' in number:
        cnt += 1

print(num)