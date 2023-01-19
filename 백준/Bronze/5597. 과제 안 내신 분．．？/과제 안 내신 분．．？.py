# 1에서 30까지 리스트
one_to_thirty = list(range(1, 31))

# 제출자 리스트
sub_lst = []
for _ in range(28):
    sub_lst.append(int(input()))

# 1~30 집합
set_1_to_30 = set(one_to_thirty)

# 제출자 집합
set_sub_lst = set(sub_lst)

# 차집합(미제출자) 구하기
not_sub = set_1_to_30 - set_sub_lst

# 집합을 리스트로
not_sub_lst = list(not_sub)

# 리스트 번호 순서대로 정렬
not_sub_lst.sort()

# 번호 순서대로 출력
for i in not_sub_lst:
    print(i)