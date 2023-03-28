# 백준 1062. 가르침

import sys
from itertools import combinations
input = sys.stdin.readline


N, K = map(int, input().split())
common = {'a', 'n', 't', 'i', 'c'}
words = [set(input().rstrip()[4:-4]) - common for _ in range(N)]     # 단어별 공통 글자 외에 배워야 할 글자 집합

K -= 5      # 공통 글자는 배웠다 치고

if K < 0:   # 공통 글자 다 못 배웠을 경우
    ans = 0
else:       # 공통 글자까지는 다 배웠을 경우
    words = [set(map(lambda x: ord(x) - ord('a'), words[i])) for i in range(N)]    # 숫자로 변환
    common = set(map(lambda x: ord(x) - ord('a'), common))  # 공통 글자 숫자 변환
    letters = [i for i in range(26) if i not in common]     # 공통 글자 제외한 글자

    ans = 0
    for comb in combinations(letters, K):   # 21개 글자 중 K개 선택
        learned = 0
        for letter in comb:     # 배운 글자 조합 비트마스크
            learned |= 1 << letter

        cnt = 0
        for word in words:      # 단어들
            word_bit = 0
            for char in word:   # 단어별 비트마스크
                word_bit |= 1 << char
            if learned | word_bit == learned:
                cnt += 1
        ans = max(ans, cnt)
print(ans)

