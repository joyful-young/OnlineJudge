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

# 수의 개수 N
N = int(input())
# 데이터 입력
input_data = list(map(int, input().split()))
# 소수의 개수
cnt = 0

for number in input_data:
    # 소수 판별해서 True이면
    if isPrime(number):
        # 카운트 증가
        cnt = cnt + 1
# 출력
print(cnt)
