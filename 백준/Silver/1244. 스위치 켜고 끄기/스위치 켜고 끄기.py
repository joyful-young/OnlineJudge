# 백준 1244. 스위치 켜고 끄기
import sys
input = sys.stdin.readline


def boy(num):
    for i in range(N):
        if (i + 1) % num == 0:  # 스위치 번호가 num의 배수
            switch[i] ^= 1      # toggle


def girl(num):
    switch[num - 1] ^= 1    # 일단 num 번호 스위치는 무조건 상태 바꿈
    for i in range(N):
        l, r = num - 1 - i, num - 1 + i     # num 중심으로 대칭인 왼쪽 오른쪽
        if 0 <= l and r < N and switch[l] == switch[r]:    # 인덱스가 범위 내이고 스위치 상태 같으면
            switch[l] ^= 1
            switch[r] ^= 1
        else:       # 만족하지 않는 게 나오면 거기서 stop
            break


N = int(input())    # 스위치 수
switch = list(map(int, input().split()))
M = int(input())    # 학생 수
for _ in range(M):
    s, n = map(int, input().split())
    if s == 1:  # 남학생
        boy(n)
    else:       # 여학생
        girl(n)

for i in range(N):
    print(switch[i], end=' ')
    if (i + 1) % 20 == 0:
        print()
