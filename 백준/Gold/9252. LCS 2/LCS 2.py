str1 = input()
str2 = input()
length1 = len(str1)
length2 = len(str2)

dp = [[[0, ""] for _ in range(length2 + 1)] for _ in range(length1 + 1)]

for i in range(1, length1 + 1):
    for j in range(1, length2 + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j][0] = dp[i - 1][j - 1][0] + 1
            dp[i][j][1] = dp[i - 1][j - 1][1] + str1[i - 1]
        
        elif dp[i - 1][j][0] <= dp[i][j - 1][0]:
            dp[i][j][0] = dp[i][j - 1][0]
            dp[i][j][1] = dp[i][j - 1][1]
            
        else:
            dp[i][j][0] = dp[i - 1][j][0]
            dp[i][j][1] = dp[i - 1][j][1]

lcs_length = dp[length1][length2][0]
print(lcs_length)
if lcs_length != 0:
    print(dp[length1][length2][1])
    