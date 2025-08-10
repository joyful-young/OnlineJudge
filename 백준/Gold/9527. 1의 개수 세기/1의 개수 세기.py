A, B = map(int, input().split())

n = 64
# prefix_sum[i]: 2^(i) - 1 까지의 1의 개수. f(2^i - 1)
prefix_sum = [0] * n
for i in range(1, n):
    prefix_sum[i] += 2 * prefix_sum[i - 1] + 2 ** (i - 1)


def func(x):
    ones = 0
    while x > 0:
        # x 이하의 2^(i) - 1 꼴 수 중 가장 큰 값이 되도록
        # 2^(power) - 1
        power = 0
        temp = x + 1
        while temp > 1:
            temp >>= 1
            power += 1

        ones += prefix_sum[power]
        # 나머지 2^(power) ~ x 까지 개수
        remained = x - (2 ** power - 1)
        # 그 숫자들의 맨 앞 1을 센다고 생각
        ones += remained
        # 그 숫자들은 각각 2^(power)로 나누어서 0 ~ x % (2^(power))를 구한다고 생각
        x = remained - 1
    return ones

print(func(B) - func(A - 1))