# SWEA 2503. 숫자 야구

import sys
input = sys.stdin.readline


def strike(s, n):
    for i in range(M):
        if possible[i]:
            cnt = 0
            for j in range(3):      # n의 자리수 세 자리
                for k in range(3):  # num_lst[i]의 자리수 세 자리
                    if j == k and n[j] == num_lst[i][k]:    # 자리수가 같고 값도 같으면 스트라이크
                        cnt += 1
            if cnt != s:    # 스트라이크 횟수가 다를 경우 False
                possible[i] = False
    return


def ball(b, n):
    for i in range(M):      # 전체 가능 숫자에 대해 확인 num_lst[i]
        if possible[i]:        # 제외되지 않은 숫자이면
            cnt = 0
            for j in range(3):      # n의 자리수 세 자리
                for k in range(3):      # num_lst[i]의 자리수 세 자리
                    if j != k and n[j] == num_lst[i][k]:    # 다른 자리지만 같은 값이 있으면
                        cnt += 1
            if cnt != b:        # ball 횟수와 다르면 check를 False로
                possible[i] = False
    return


# 가능한 숫자 리스트 만들기
num_lst = [0 for _ in range(9 * 8 * 7)]
M = len(num_lst)
possible = [True for _ in range(M)]    # 가능성

tmp = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or i == k or j == k:
                continue
            else:
                num_lst[tmp] = str(100 * i + 10 * j + k)
                tmp += 1

# print(num_lst)

# 입력 받기
N = int(input())
for _ in range(N):
    num, S, B = map(int, input().split())   # 숫자, 스트라이트, 볼
    num_str = str(num)      # 숫자 string으로
    strike(S, num_str)
    ball(B, num_str)

print(possible.count(True))