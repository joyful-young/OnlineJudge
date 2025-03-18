import sys
input = sys.stdin.readline


def prefix_len(word1, word2):
    min_length = min(len(word1), len(word2))
    for i in range(min_length):
        if word1[i] != word2[i]:
            return i
    return min_length



N = int(input())
words = [input().rstrip() for _ in range(N)]
sorted_words = sorted([[words[i], i] for i in range(N)])


ans = prefix_len(sorted_words[0][0], sorted_words[1][0])
prefix_dict = {} if ans == 0 else {sorted_words[0][0][:ans]: [sorted_words[0][1], sorted_words[1][1]]}

idx = 2
while idx < N:
    p_len = prefix_len(sorted_words[idx - 1][0], sorted_words[idx][0])
    
    if p_len > ans:
        ans = p_len
        prefix_dict = {sorted_words[idx][0][:p_len]: [sorted_words[idx - 1][1], sorted_words[idx][1]]}
    elif p_len == ans:
        # 연이어서 접두사가 같은 경우
        if sorted_words[idx][0][:p_len] in prefix_dict:
            prefix_dict[sorted_words[idx][0][:p_len]].append(sorted_words[idx][1])
        # 글자가 다른데 접두사 길이가 같은 경우
        else:
            prefix_dict[sorted_words[idx][0][:p_len]] = [sorted_words[idx - 1][1], sorted_words[idx][1]]
    idx += 1

word_idx_lists = [sorted(idx_list) for idx_list in prefix_dict.values()]
if len(word_idx_lists) > 1:
    word_idx_lists.sort()
    
print(words[word_idx_lists[0][0]])
print(words[word_idx_lists[0][1]])
    