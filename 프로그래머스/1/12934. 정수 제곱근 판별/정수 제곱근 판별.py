def solution(n):
    sqrt_n = n ** 0.5
    if sqrt_n.is_integer():
        x = int(sqrt_n)
        return (x + 1) ** 2
    
    return -1