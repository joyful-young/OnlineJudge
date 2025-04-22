DIV = 1000000007

p = {0: 1, 1: 2}

def power(n):
    if n in p:
        return p[n]
    
    if n % 2:
        p[n] = (2 * power(n - 1)) % DIV
    else:
        t = power(n // 2) % DIV
        p[n] = (t * t) % DIV
    return p[n]
        
T = int(input())
for _ in range(T):
    n = int(input())
    if n <= 2:
        print(1)
    else:
        print(power(n - 2))
