# 'A' = 65, 'Z' = 90

# 단어 입력, 대문자로 바꾸기, 문자 하나씩 나누기
letters = list(input().upper())

# 아스키코드 변환
ord_letters = list(map(ord, letters))

# 문자 나온 횟수 세기
letters_count = [0 for _ in range(65, 91)]
for letter in ord_letters:
    for i in range(65, 91):
        if letter == i:
            letters_count[i - 65] += 1

# 제일 많이 나온 문자의 나온 횟수
max_letter_count = max(letters_count)

# 문자 카운트 리스트 중 최대 카운트가 하나보다 많으면 '?' 출력
if letters_count.count(max_letter_count) > 1:
    print('?')

# 최댓값이 하나뿐이면 그 최댓값의 인덱스 구해서 그에 해당하는 문자 구함
else:
    max_idx = letters_count.index(max_letter_count)
    print(chr(max_idx + 65))