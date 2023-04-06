# 백준 1018. 체스판 다시 칠하기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())        # 행, 열
arr = [input().rstrip() for _ in range(N)]

minV = 2500
for i in range(N - 7):
    for j in range(M - 7):      # 체스판의 왼쪽 상단 결정
        tmp = 0
        # 왼쪽 상단을 흰색으로 결정할 경우
        for k in range(8):
            for l in range(8):
                if (k + l) % 2:     # k + l이 홀수이면 검은색이어야
                    if arr[i + k][j + l] != 'B':        # 검은색이 아니면
                        tmp += 1
                else:               # k + l이 짝수이면 흰색이어야
                    if arr[i + k][j + l] != 'W':        # 흰색이 아니면
                        tmp += 1
        minV = min(minV, tmp)

        tmp = 0
        # 왼쪽 상단을 검은색으로 결정할 경우
        for k in range(8):
            for l in range(8):
                if (k + l) % 2:     # k + l이 홀수이면 흰색이어야
                    if arr[i + k][j + l] != 'W':        # 흰색이 아니면
                        tmp += 1
                else:               # k + l이 짝수이면 검은색이어야
                    if arr[i + k][j + l] != 'B':        # 검은색이 아니면
                        tmp += 1
        minV = min(minV, tmp)

print(minV)