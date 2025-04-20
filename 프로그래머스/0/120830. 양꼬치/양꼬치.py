def solution(n, k):
    service_drink = n // 10
    return 12000 * n + 2000 * (k - service_drink)