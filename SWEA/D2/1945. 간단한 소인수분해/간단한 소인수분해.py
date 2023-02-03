T = int(input())
for tc in range(1, T + 1):
    number = int(input())
    primes = [2, 3, 5, 7, 11]   # 소인수

    ans = [0] * 5   # 지수 초기화

    for i in range(4, -1, -1):      # primes와 ans의 인덱스
        while number % primes[i] == 0:      # 나누어 떨어지는 한
            number //= primes[i]    # 나누고
            ans[i] += 1             # 지수 1 증가

    print(f'#{tc}', *ans)
