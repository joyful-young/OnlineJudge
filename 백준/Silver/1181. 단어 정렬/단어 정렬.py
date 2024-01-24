# 단어 정렬
N = int(input())

word_lists = [[] for _ in range(51)]

for _ in range(N):
    word = input()
    if word not in word_lists[len(word)]:
        word_lists[len(word)].append(word)

ans = []
for word_list in word_lists:
    if not word_list:
        continue
    if len(word_list) > 1:
        word_list.sort()

    ans += word_list

for word in ans:
    print(word)
