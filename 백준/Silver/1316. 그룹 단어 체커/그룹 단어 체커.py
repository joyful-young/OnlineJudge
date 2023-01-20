# 연속되는 문자를 하나의 문자로 생각
# aabbbccb -> abcb -> b가 2개 있으므로 그룹단어 아님

# 그룹 단어인지 판단하는 함수 정의
def is_group_word(word):
    # 첫 번째 문자 리스트에 집어넣고 시작
    letter_list = [word[0]]
    for i in range(1, len(word)):
        # 문자가 바로 이전 문자와 같으면 리스트에 넣지 않음
        if word[i] == word[i-1]:
            pass
        # 바로 이전 문자와 다를 경우 리스트에 넣음
        else:
            letter_list.append(word[i])
    # 이렇게 만든 리스트와 그것으로 만든 집합의 길이가 같으면(중복 문자 없음) 그룹단어
    letter_set = set(letter_list)

    if len(letter_list) == len(letter_set):
        return True
    else:
        return False

import sys

# 단어의 개수
N = int(input())

# 그룹 단어 개수 세기
cnt = 0

for _ in range(N):
    word = sys.stdin.readline()
    if is_group_word(word):
        cnt = cnt + 1

print(cnt)