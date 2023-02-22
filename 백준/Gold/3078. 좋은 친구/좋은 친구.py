# 백준 3078. 좋은 친구

from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())

name_len = [0] * 21     # 글자수 2 ~ 20글자. 인덱스 맞추기     # 글자수 i인 사람 수 세기 위한 배열
students = deque()
cnt = 0

for i in range(N):
    length = len(sys.stdin.readline().rstrip())     # 이름 길이
    students.append(length)     # 큐에 넣기
    name_len[length] += 1       # 이름 길이 length인 사람 1명 증가
    if students and len(students) > K:      # 큐에 이름이 있고 큐 길이가 K를 넘으면
        s1 = students.popleft()         # 하나 빼서
        name_len[s1] -= 1               # 그 학생 이름 길이 카운트 빼고
        cnt += name_len[s1]             # 그 학생 이름 길이 남은 카운트가 그 학생과 좋은 친구인 학생 수

while students:                 # 마지막 입력까지 다 넣었으면 큐가 빌 때까지
    s1 = students.popleft()     # 하나 빼서
    name_len[s1] -= 1
    cnt += name_len[s1]         # 카운트 추가

print(cnt)