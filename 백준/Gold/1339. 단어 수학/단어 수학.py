# 백준 1339. 단어 수학

import sys
input = sys.stdin.readline

N = int(input())
char_dic = {}
for _ in range(N):
    word = input().rstrip()
    for i in range(len(word)):
        if word[i] not in char_dic:
            char_dic[word[i]] = 10 ** (len(word) - i - 1)
        else:
            char_dic[word[i]] += 10 ** (len(word) - i - 1)

# print(char_dic)
char_lst = sorted(list(char_dic.items()), key=lambda x: x[1], reverse=True)

num = 9
ans = 0
for i in range(len(char_lst)):
    ans += char_lst[i][1] * num
    num -= 1

print(ans)