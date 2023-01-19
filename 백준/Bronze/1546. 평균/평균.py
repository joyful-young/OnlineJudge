# 과목 수
N = int(input())

# 원래 점수
scores = list(map(int, input().split()))

# 최고점
max_score = max(scores)

# 새로 고친 점수
new_scores = [score / max_score * 100 for score in scores]

# 새로운 평균
new_avg = sum(new_scores) / N

# 출력
print(new_avg)