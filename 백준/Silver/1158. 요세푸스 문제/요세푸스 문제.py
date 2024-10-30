# 1158. 요세푸스 문제
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().strip().split())
numbers = deque([str(i) for i in range(1, N + 1)])
ans = []
while numbers:
    for i in range(K):
        if i == K - 1:
            ans.append(numbers.popleft())
        else:
            numbers.append(numbers.popleft())

ret = "<" + ", ".join(ans) + ">"
print(ret)