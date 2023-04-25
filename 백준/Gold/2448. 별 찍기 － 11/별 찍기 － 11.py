# 백준 2448. 별 찍기 - 11

def star(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']

    rlt = []
    tmp = star(n // 2)

    for row in tmp:
        rlt.append(' ' * (n // 2) + row + ' ' * (n // 2))

    for row in tmp:
        rlt.append(row + ' ' + row)

    return rlt

N = int(input())

stars = star(N)

print('\n'.join(stars))