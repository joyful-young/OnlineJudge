# 백준 15661. 링크와 스타트

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 스타트 팀에 뽑힌 걸 1, 링크 팀에 뽑힌 걸 0으로 표현
minV = 40000
for i in range(1, (1 << (N - 1))):  # 모두 다 링크 팀 제외, 모두 다 스타트팀 제외
    # 숫자 i가 정해지면 팀이 정해짐
    tmp = 0     # 두 팀의 차이
    for j in range(N - 1):      # 정해진 팀에서 j번째, k번째 사람 두명 조합
        for k in range(j + 1, N):
            if i & (1 << j) and i & (1 << k):   # 둘 다 스타트팀
                tmp += arr[j][k] + arr[k][j]
            if not (i & (1 << j)) and not (i & (1 << k)):   # 둘 다 링크 팀
                tmp -= arr[j][k] + arr[k][j]
    minV = min(minV, abs(tmp))      # 두 팀 능력치 차이 최솟값으로 갱신

print(minV)