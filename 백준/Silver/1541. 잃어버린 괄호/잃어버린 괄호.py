# 백준 1541. 잃어버린 괄호

minus_split = input().split('-')    # 가장 처음과 마지막 문자는 숫자. 맨 앞에 - 올 경우 없음
# '-' 기준으로 나눠서 나머지는 묶어서 더해 빼버림

N = len(minus_split)

num = [0] * N

for i in range(N):
    if '+' in minus_split[i]:
        num[i] = sum(list(map(int, minus_split[i].split('+'))))
    else:
        num[i] = int(minus_split[i])

ans = num[0]
for i in range(1, N):
    ans -= num[i]

print(ans)