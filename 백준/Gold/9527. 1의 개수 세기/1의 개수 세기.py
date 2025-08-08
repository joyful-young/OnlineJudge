# 9527. 1의 개수 세기
A, B = map(int, input().split())

def count(num):
    ans = 0
    while num > 0:
        power = 0
        temp = num + 1
        while temp > 1:
            temp >>= 1
            power += 1

        ans += acc_sum[power]
        diff = num - (2 ** power - 1)
        ans += diff
        num = diff - 1

    return ans


n = 64
# 누적합 a_n = 2 * a_(n-1) + 2^(n-1)
acc_sum = [0 for _ in range(n)]
for i in range(1, n):
    acc_sum[i] = 2 * acc_sum[i - 1] + 2 ** (i - 1)

print(count(B) - count(A - 1))
