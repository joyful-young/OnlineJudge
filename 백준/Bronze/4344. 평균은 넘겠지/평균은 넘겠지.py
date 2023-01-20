# 테스트 케이스 개수
C = int(input())

import sys

# 케이스마다 반복
for _ in range(C):
    input_data = list(map(int, sys.stdin.readline().split()))
    
    # 학생 수
    stu_num = input_data[0]
    
    # 점수
    scores = input_data[1:]

    # 평균 점수
    avg_score = sum(scores) / len(scores)

    # 평균 넘는 학생 수 세기
    over_avg = 0

    for score in scores:
        if score > avg_score:
            over_avg = over_avg + 1
        else:
            pass
    
    # 비율 구하기
    ratio = over_avg / stu_num * 100

    # 출력
    print(f'{ratio:0.3f}%')
