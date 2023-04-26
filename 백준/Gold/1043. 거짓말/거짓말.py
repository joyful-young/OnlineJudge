# 백준 1043. 거짓말
import sys
input = sys.stdin.readline


def find_set(x):
    while rep[x] != x:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


N, M = map(int, input().split())
know_truth = list(map(int, input().split()))
if know_truth[0] == 0:      # 진실 아는 사람 없으면
    print(M)        # 모든 파티에서 과장된 얘기
else:
    know_truth = know_truth[1:]     # 진실 아는 사람 번호 리스트

    # make_set
    rep = [i for i in range(N + 1)]     # 사람 번호 1부터 N
    parties = []
    # 같은 파티에 오는 사람들 집합으로 묶어서
    for _ in range(M):      # M개의 파티
        tmp = list(map(int, input().split()))
        if tmp[0] == 1:     # 파티 오는 사람 1명이면 넘어감
            parties.append(tmp[1:])
            continue

        # 한 파티 참석자 모두 같은 집합으로 묶기
        cnt = tmp[0]        # 파티 참석자 수
        people = tmp[1:]
        parties.append(people)
        for i in range(1, cnt):         # 같은 집합으로 묶기
            union(people[0], people[i])

    # print(rep)

    # 진실 아는 사람 포함된 집합은 제외하고
    # know_truth에 있는 사람들과 대표 원소 같은 것은 다 제외
    # 남은 집합들에 있는 사람들 모아서
    lst = []
    for person_num in range(1, N + 1):  # 1번 ~ N번 사람
        rep_elem = find_set(person_num)
        for know_person in know_truth:      # 진실 아는 사람이 포함된 집합의 대표원소
            if rep_elem == find_set(know_person):   # 진실을 아는 사람과 같은 집합에 포함된 사람이면
                break
        else:   # 진실을 아는 사람과 같은 집합에 속하지 않을 경우
            lst.append(person_num)      # 번호 넣기

    # print(lst)
    # print(parties)

    # 파티마다 오는 사람 집합이 그 사람들 집합에 포함되면
    # 그건 과장된 얘기 할 수 있는 파티
    ans = 0
    lst = set(lst)
    for party in parties:
        party = set(party)
        if party.issubset(lst):
            ans += 1

    print(ans)
