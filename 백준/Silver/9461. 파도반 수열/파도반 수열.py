# 9461. 파도반 수열
def solution(n):
    if ans[n] != 0:
        return ans[n]

    ans[n] = solution(n - 5) + solution(n - 1)
    return ans[n]

ans = [0, 1, 1, 1, 2, 2] + [0 for _ in range(95)]
T = int(input())
for _ in range(T):
    print(solution(int(input())))
