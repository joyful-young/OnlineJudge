import sys

input = sys.stdin.readline

def solution():

    def divide(coins, total):
        if total%2:
            return 0
        h = 1<<(total//2)
        bit = 1
        for coin, count in coins:
            for _ in range(count):
                bit |= bit<<coin
                if bit&h:
                    return 1
        return 0

    for _ in range(3):
        N = int(input())
        coins = []
        total = 0
        for _ in range(N):
            coin, count = map(int, input().split())
            coins.append((coin, count))
            total += coin*count
        print(divide(coins, total))

solution()