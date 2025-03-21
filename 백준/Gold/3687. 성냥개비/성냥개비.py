import sys
input = sys.stdin.readline

T = int(input())
MAX_N = 101

def sort_digits(number_str):
    digits = sorted(number_str)
    if digits[0] == "0":
        for i in range(1, len(digits)):
            if digits[i] != "0":
                digits[0], digits[i] = digits[i], digits[0]
                break
    return "".join(digits)

# 최솟값
min_v = [0 for _ in range(MAX_N)]
min_v[2] = "1"
min_v[3] = "7"
min_v[4] = "4"
min_v[5] = "2"
min_v[6] = "6"
min_v[7] = "8"

match_digit = [
    (2, "1"),
    (3, "7"),
    (4, "4"),
    (5, "2"),
    (6, "0"),
    (7, "8")
]

for i in range(8, MAX_N):
    candidates = []
    for match, digit in match_digit:
        if i - match >= 2 and min_v[i - match] != 0:
            candidate = min_v[i - match] + digit
            candidates.append(sort_digits(candidate))
    if candidates:
        min_v[i] = min(candidates, key=lambda x: (len(x), x))


# 최댓값
max_v = [0 for _ in range(MAX_N)]
for i in range(2, MAX_N):
    digits = ["1" for _ in range(i // 2)]
    if i % 2 == 1:
        digits[0] = "7"
    max_v[i] = "".join(digits)

for _ in range(T):
    N = int(input())
    print(min_v[N], max_v[N])
    