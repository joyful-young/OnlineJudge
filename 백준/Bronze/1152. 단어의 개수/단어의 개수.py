# 단어 소문자로 바꿔서 리스트에
words = (input().lower()).split()

# 단어 딕셔너리
words_dic = {}

# 단어별 개수 딕셔너리
for word in words:
    if word in words_dic:
        words_dic[word] += 1
    else:
        words_dic[word] = 1

# 딕셔너리 value만 모아서 리스트로
num_of_words = list(words_dic.values())

# 단어 전체 개수 출력
print(sum(num_of_words))