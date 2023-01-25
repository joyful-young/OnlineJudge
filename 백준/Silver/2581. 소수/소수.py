# 소수 판별 함수
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True

# M, N 입력
M = int(input())
N = int(input())

# 소수 리스트 생성
primenum = []

# M 이상 N 이하의 i에 대해
for i in range(M, N + 1):
    # i가 소수이면
    if isPrime(i):
        # 소수 리스트에 추가
        primenum.append(i)

if primenum != []:
    # 소수 합
    print(sum(primenum))
    # 최소 소수
    print(min(primenum))
else:
    print(-1)
