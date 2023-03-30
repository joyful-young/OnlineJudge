# 백준 1722. 순열의 순서


N = int(input())
arr = list(map(int, input().split()))
number = list(range(1, (N + 1)))

lst = list(range(N, 0, -1))
for i in range(N - 1, 0, -1):
    lst[i - 1] *= lst[i]

if arr[0] == 1:  # k번째 순열 구하기
    k = arr[1]
    k -= 1
    perm = []
    for i in range(1, N):
        idx, k = divmod(k, lst[i])
        perm.append(number.pop(idx))
    perm += number
    print(*perm)
else:       # 몇번째 순열인가
    perm = arr[1:]
    k = 1
    for i in range(N - 1):
        idx = number.index(perm[i])
        k += idx * lst[i + 1]
        number.pop(idx)
    print(k)