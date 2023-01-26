# 에라토스테네스의 체
# 백준 1929

# M, N 입력
M, N = map(int, input().split())

# 0이상 N 이하의 정수에 대해 소수 판별 리스트 만들기
# 인덱스 이용하기가 0 포함하는 게 편함
check = [False, False] + [True] * (N - 1)

# 판별된 소수 넣을 리스트
is_prime = []

# N 이하의 수 판별
for number in range(N + 1):
    # 소수 판별 리스트에서 True이면
    if check[number]:
        # # 소수 리스트에 추가
        # is_prime.append(number)
        # 그 소수의 배수들을 False로
        for i in range(number * 2, N + 1, number):
            check[i] = False
        
        # 답을 바로 구하려면
        # number가 M 이상인 경우에만 is_prime에 추가
        if number >= M:
            is_prime.append(number)

for prime_number in is_prime:
    print(prime_number)