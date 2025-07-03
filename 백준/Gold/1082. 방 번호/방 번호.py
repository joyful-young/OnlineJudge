import sys
input = sys.stdin.readline

N = int(input())
prices = list(map(int, input().split()))
M = int(input())


# 자릿수를 최대로
min_p_digit = min(range(N), key=lambda x: prices[x])
remaining_money = M
if N == 1:
    ans = [0]
    remaining_money -= prices[0]
elif min_p_digit == 0:
    # 0이 아닌 수 중 제일 싼 숫자
    non_zero_min_p_dg = min(range(1, N), key=lambda x: prices[x])
    
    if prices[non_zero_min_p_dg] > M:
        ans = [min_p_digit]
        remaining_money -= prices[min_p_digit]
    else:
        zeros = (M - prices[non_zero_min_p_dg]) // prices[min_p_digit]
        ans = [non_zero_min_p_dg] + [min_p_digit] * zeros
        remaining_money -= prices[non_zero_min_p_dg]
        remaining_money -= prices[min_p_digit] * zeros
else:
    num_of_digits = M // prices[min_p_digit]
    ans = [min_p_digit] * num_of_digits
    remaining_money -= prices[min_p_digit] * num_of_digits

# 더 큰 수로 바꿀 수 있으면 바꾸기
for idx in range(len(ans)):
    digit = ans[idx]
    for bigger_digit in range(N - 1, digit, -1):
        diff = prices[bigger_digit] - prices[digit]
        if diff <= remaining_money:
            ans[idx] = bigger_digit
            remaining_money -= diff
            break

print("".join(map(str, ans)))