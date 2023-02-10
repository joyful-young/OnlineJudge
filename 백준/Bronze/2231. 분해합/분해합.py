# 백준 2231. 분해합

N = int(input())

for i in range(1, N):
    num = i
    sum_of_num = i
    while num > 0:
        sum_of_num += num % 10
        num = num // 10

    if sum_of_num == N:
        print(i)
        break
else:
    print(0)
