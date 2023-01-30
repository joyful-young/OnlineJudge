import sys

# N, K 입력
N, K = map(int, sys.stdin.readline().split())

# 동전 종류 리스트 내림차순
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline()))
A.reverse()

# 필요한 동전의 개수
cnt = 0


for i in A:
    # K가 0이되면 그만두기
    if K == 0:
        break
    # K를 i로 나눈 몫을 동전 수에 더하고 나머지를 K로
    else:
        cnt = cnt + K // i
        K = K % i
# 동전 개수 출력
print(cnt)