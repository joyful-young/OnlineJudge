str1 = input()
str2 = input()
length1 = len(str1)
length2 = len(str2)

dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]

for i in range(1, length1 + 1):
    for j in range(1, length2 + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# LCS 문자열 찾기
i, j = length1 - 1, length2 - 1
lcs = []
while i >= 0 and j >= 0:
    if str1[i] == str2[j]:
        lcs.append(str1[i])
        i -= 1
        j -= 1
    elif dp[i][j + 1] >= dp[i + 1][j]:
        i -= 1
    else:
        j -= 1

print(dp[length1][length2])
if dp[length1][length2] != 0:
	print("".join(reversed(lcs)))
