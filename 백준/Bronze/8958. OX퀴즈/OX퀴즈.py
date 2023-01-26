# n개 연속이면 1에서 n까지 더한 만큼의 점수를 얻음
# 80보다 작은 문자열. 연속해서 맞은 개수는 최대 79

# 0 ~ 79 의 0부터 n까지의 합 리스트
sum_list = [sum(list(range(n + 1))) for n in range(80)]

# 테스트케이스 입력
T = int(input())

for test_case in range(T):
    # 퀴즈 결과 입력
    quiz_rlt = input()
    
    # x를 공백으로 대체
    o_only = quiz_rlt.replace('X', ' ')
    
    # 연속된 O의 묶음 리스트
    o_list = o_only.split() # x만 있으면 빈 리스트

    # 연속된 o의 개수 리스트
    num_of_o = [len(i) for i in o_list] # x만 있으면 빈 리스트

    # o의 개수에 따라 그 점수 구해 더하기
    result = 0
    for i in num_of_o:
        result += sum_list[i] # num_of_o가 빈 리스트면 아예 반복 안 하는 건가
    print(result)