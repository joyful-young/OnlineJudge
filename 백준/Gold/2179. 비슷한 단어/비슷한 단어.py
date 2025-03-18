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
sorted_idxs = sorted(range(N), key=lambda i: words[i])


ans = prefix_len(words[sorted_idxs[0]], words[sorted_idxs[1]])
prefix_dict = {} if ans == 0 else {words[sorted_idxs[0]][:ans]: [sorted_idxs[0], sorted_idxs[1]]}

for i in range(2, N):
    p_len = prefix_len(words[sorted_idxs[i - 1]], words[sorted_idxs[i]])
    if p_len > ans:
        ans = p_len
        prefix_dict = {words[sorted_idxs[i]][:p_len]: [sorted_idxs[i - 1], sorted_idxs[i]]}
    elif p_len == ans:
        # 연이어서 접두사가 같은 경우
        if words[sorted_idxs[i]][:p_len] in prefix_dict:
            prefix_dict[words[sorted_idxs[i]][:p_len]].append(sorted_idxs[i])
        # 글자가 다른데 접두사 길이가 같은 경우
        else:
            prefix_dict[words[sorted_idxs[i]][:p_len]] = [sorted_idxs[i - 1], sorted_idxs[i]]

word_idx_lists = [sorted(idx_list) for idx_list in prefix_dict.values()]
if len(word_idx_lists) > 1:
    word_idx_lists.sort()
    
print(words[word_idx_lists[0][0]])
print(words[word_idx_lists[0][1]])