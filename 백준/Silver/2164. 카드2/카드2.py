# 백준 2164. 카드2

from collections import deque

N = int(input())

cards = deque(list(range(1, N + 1)))

while len(cards) > 1:
    cards.popleft()
    cards.rotate(-1)

print(cards[0])