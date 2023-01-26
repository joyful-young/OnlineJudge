# 에라토스테네스의 체
# 백준 2960

# N, K 입력
N, K = map(int, input().split())

# 0이상 N 이하의 정수에 대해 소수 판별 리스트 만들기
# 인덱스 이용하기가 0 포함하는 게 편함
check = [False, False] + [True] * (N - 1)

# 판별된 소수 넣을 리스트
is_prime = []
# 지우는 횟수 카운트
cnt = 0

# N 이하의 수 판별
for number in range(N + 1):
    # 소수 판별 리스트에서 True이면
    if check[number]:
        # 소수 리스트에 추가
        is_prime.append(number)
        # 그 소수와 그 소수의 배수들을 False로
        for i in range(number, N + 1, number):
            # 지워지지 않았을 경우(True일 경우) False로 만들고 카운트 1 증가
            if check[i]:
                check[i] = False
                cnt += 1
            # 이미 False이면 카운트할 필요 없음
            else:
                pass
            
            # 지운 횟수가 K와 같으면 그때 False 된 수 프린트하고 반복 종료
            if cnt == K:
                print(i)
                break