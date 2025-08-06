import sys
input = sys.stdin.readline


T = 3
for _ in range(T):
    N = int(input())
    coins = []
    
    total = 0
    for _ in range(N):
        coin, cnt = map(int, input().split())
        coins.append((coin, cnt))
        total += coin * cnt

    q, r = divmod(total, 2)
    if r != 0:
        print(0)
        continue

    dp = [False] * (q + 1)
    dp[0] = True

    for i in range(N):
        coin, cnt = coins[i]

        for j in range(q, coin - 1, -1):
            if dp[j - coin]:
                for k in range(cnt):
                    if j + coin * k > q:
                        break
                        
                    dp[j + coin * k] = True

        if dp[q]:
            print(1)
            break
    else:
        print(0)