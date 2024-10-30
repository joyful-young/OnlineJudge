# 1158. 요세푸스 문제
N, K = map(int, input().split())
numbers = [str(i) for i in range(1, N + 1)]
idx = 0
ans = []
while numbers:
    idx += (K - 1)
    idx %= len(numbers)
    ans.append(numbers.pop(idx))
ret = "<" + ", ".join(ans) + ">"
print(ret)