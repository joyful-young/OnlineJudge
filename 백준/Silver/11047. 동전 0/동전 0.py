import sys

# N, K 입력
N, K = map(int, sys.stdin.readline().split())

# 동전 종류 리스트
A = []
for _ in range(N):
    A.insert(0, int(sys.stdin.readline()))


# 필요한 동전의 개수
cnt = 0

# K = 0이 될 때까지 반복
while K > 0:
    # K에서 A 원소를 큰 것부터 음수가 되지 않고 뺄 수 있으면 빼기
    # K가 A[0] 이상이면 K - A[0]
    while K >= A[0]:
        K -= A[0]
        # 뺄 때마다 동전 개수 증가
        cnt += 1
    # 다 빼고 나면 리스트에서 그 원소 삭제
    else:
        del A[0]

# 동전 개수 출력
print(cnt)