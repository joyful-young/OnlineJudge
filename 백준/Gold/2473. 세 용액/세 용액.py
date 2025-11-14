import sys
input = sys.stdin.readline

N = int(input())
solutions = list(map(int, input().split()))
solutions.sort()


def solve():
    min_abs = 3_000_000_000
    answer = []

    for i in range(N - 2):
        # i번 용액 우선 선택 고정, 나머지 두 개 골라서 합 구해보기
        left, right = i + 1, N - 1
        while left < right:
            s = solutions[i] + solutions[left] + solutions[right]
            
            if abs(s) < min_abs:
                min_abs = abs(s)
                answer = [solutions[i], solutions[left], solutions[right]]
                if s == 0:
                    return answer

            if s > 0:
                right -= 1
            else:
                left += 1

    return answer


print(*solve())