# 백준 2447. 별 찍기 - 10

def star(n):
    if n == 3:
        return ['***', '* *', '***']

    rlt = []
    tmp = star(n // 3)      # 이전 단위 정사각형

    for row in tmp:         # 이전 정사각형 3개를 그대로
        rlt.append(row * 3)

    for row in tmp:         # 정사각형 1개 + 공백 + 정사각형 1개
        rlt.append(row + ' ' * (n // 3) + row)

    for row in tmp:
        rlt.append(row * 3)

    return rlt


N = int(input())

stars = star(N)
# print(stars)
print('\n'.join(stars))

# for row in stars:
#     print(row)
