# 백준 14889. 스타트와 링크 - swea 요리사 문제랑 같음
# itertools

from itertools import combinations

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

# 사람들 중 N // 2 명 고른 부분집합 만들기
start_team = list(combinations(range(N), N // 2))

link_team = [list(set(range(N)) - set(start_team[i])) for i in range(len(start_team))]

# 스타트 팀, 링크 팀 능력치 차이 최솟값 구하기
minV = 10000

for k in range(len(start_team)):
    start = 0
    link = 0

    # 정해진 스타트 팀에서 두 명 뽑는 조합
    for i, j in combinations(start_team[k], 2):
        start += arr[i][j] + arr[j][i]      # 팀 능력치 구하기

    # 정해진 링크 팀에서 두 명 뽑는 조합
    for i, j in combinations(link_team[k], 2):
        link += arr[i][j] + arr[j][i]

    minV = min(minV, abs(start - link))

print(minV)